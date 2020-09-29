
from cheesechain import CheeseChain
from socket import socket, create_connection
from threading import Thread
import pickle
import os
import time

ServerIP = "172.18.250.104" #Ip of the tracker
ServerPort=9876             #Port of the tracker

IP = "172.18.250.104"      #Ip of this client


#Below are the commands for the protocol
JoinNetworkProtocol="|J|"
RequestClientListProtocol="|C|"
PingProtocol="|P|"
TransmitCheese="|T|"
RecieveCheese="|R|"
OkayProtocol="|O|"
EndProtocol="|E|"
DropProtocol="|D|"
InvalidProtocol="|I|"
NoneProtocol="|N|"


class Client:
    CHAIN_PATH = str(os.path.expanduser("~")) + "/CheeseChain/.chain/"
    os.makedirs(CHAIN_PATH, exist_ok=True)

    def __init__(self, port=1112):
        self.path = Client.CHAIN_PATH + str(port)
        self.port = port
        self.ClientList = []
        self.NetworkFlag = False
        self.cheeseChain = self.Loadchainfromlocal()
    '''Function to start client and search for local cheese and cheese from 
    other clients
    '''
    def startclient(self):
        self.Loopflag = True
        def runningclient():
            self.JoinNetwork()
            while True and self.Loopflag:
                Thread(target=self.StoreCheese).start()
                Thread(target=self.getblockchain).start()
                time.sleep(30)
        Thread(target=runningclient).start()
    #Function to stop client
    def stopclient(self):
        self.Loopflag = False

    #Function to load chain from local storage
    def Loadchainfromlocal(self):
        try:
            return pickle.load(open(self.path, "rb"))
        except:
            return CheeseChain()

    #Function to store cheese in the local storage
    def StoreCheese(self):
        pickle.dump(self.cheeseChain, open(self.path, "wb"))

    #Function to parce text \r represents end of command \n represents end of data
    def parcingtext(self,conn):
        responce=b""
        readFlag=False
        while True:
            r = conn.recv(1)
            if len(r)==0:
                return None
            if r==b"\n" and readFlag:
                break
            if readFlag:
                responce += b"\r";
            if r == b"\r":
                readFlag = True;
            else:
                readFlag=False;
                responce += r;
        try:
            return responce.decode("utf-8")
        except:
            return responce

    #Function to join network from client to tracker
    def JoinNetwork(self):
        try:
            conn = create_connection((ServerIP, ServerPort))
            conn.sendall(b'|J|\r\n')
            conn.sendall(bytes(str(self.port) + '\r\n', 'utf-8'))
            conn.close()
            self.NetworkFlag = True
        except Exception as e:
            print("Error Client Joining the Network: ", e)

    '''Function to get clients from tracker.
       Client requests tracker for the active list and tracker responds with that list 
    '''
    def get_peers(self):
        try:
            conn = create_connection((ServerIP, ServerPort))
            conn.sendall(b"|C|\r\n")
            print("SENT: Get Peer Request")
            self.ClientList = []
            while True:
                l = self.parcingtext(conn)
                if l == "|E|":
                    break
                else:
                    if (l == IP + ':' + str(self.port)):
                        print((l == IP + ':' + str(self.port)))
                        print("From Server Client List", l)
                        continue
                    self.ClientList.append(l)
            print("Received Clients: ", self.ClientList)

        except Exception as e:
            print("Error While receiving Client List: ", e)

    '''Function to define threads to start this client to listen to other clients'''
    def startListening(self):
        listenerSocket = socket()
        listenerSocket.bind((IP, self.port))
        listenerSocket.listen()
        print("Client Socket is Listening", self.port)
        def listenerThread():
            while True:
                conn, addr = listenerSocket.accept()
                print("Handling the Connection", addr)
                Thread(target=self.ClientService, args=(conn,)).start()
        Thread(target=listenerThread).start()

    #Function to serve for the requests from other clients
    def ClientService(self, conn):
        l = self.parcingtext(conn)
        print("RECEIVED: ", l)
        #ping request
        if l == "|P|":
            conn.sendall(b"|O|\r\n")
            print("SENT: OK")
        #Transmission cheese request
        if l == "|T|":
            cheesedmp = self.parcingtext(conn)
            chs = pickle.loads(cheesedmp)
            print("RECEIVED Cheese: ", chs)
            if len(self.cheeseChain.stack) != chs.id:
                print("SENT: DROP Command")
                conn.sendall(b"|D|\r\n")
            else:
                status = self.cheeseChain.insertCheese(chs)
                if status:
                    print("SENT: OK Command")
                    conn.sendall(b"|O|\r\n")
                else:
                    print("SENT: INVALID Command")
                    conn.sendall(b"|I|\r\n")
        #Receiving control for cheese
        if l == "|R|":
            id = self.parcingtext(conn)
            id = int(id)
            print("RECEIVED: ", id)
            if len(self.cheeseChain.stack) > id:
                cheesedmp = pickle.dumps(self.cheeseChain.stack[id])
                conn.sendall(cheesedmp)
                conn.sendall(b"\r\n")
                print("SENT Cheese: ", self.cheeseChain.stack[id])
            else:
                conn.sendall(b"|N|\r\n")
                print("SENT: NONE")

        conn.close()
        print("Connection Closed")

    #Functionto get block chain from other clients
    def getblockchain(self):
        self.get_peers()
        for clt in self.ClientList:
            ip, port = clt.split(":")
            print("This ip and port",ip,port)
            fetchid = str(len(self.cheeseChain.stack))
            try:
                conn = create_connection((ip, port))
                conn.sendall(b'|R|\r\n')
                print("SENT: GETCheese Request")
                conn.sendall(bytes(fetchid + '\r\n', 'utf-8'))
                print("SENT: ", fetchid)
                resp = self.parcingtext(conn)
                conn.close()
                if resp == "|N|":
                    print("RECEIVED: NONE")
                    continue
                else:
                    blk = pickle.loads(resp)
                    print("RECEIVED Cheese: ", blk)
                    status = self.cheeseChain.insertCheese(blk)
                    if status:
                        print("Cheese added!")
                    else:
                        print("Cheese ignored!")
            except Exception as e:
                print("Error While Searching for Cheeses: ", e)

    #Function to broadcast a cheese when a new cheese is created
    def bradcastchain(self, id):
        def broadcasterThread():
            self.get_peers()
            cheesedmp = pickle.dumps(self.cheeseChain.stack[id])
            for mem in self.ClientList:
                ip, port = mem.split(":")
                try:
                    conn = create_connection((ip, port))
                    conn.sendall(b'|T|\r\n')
                    print("SENT: Cheese")
                    conn.sendall(cheesedmp)
                    conn.sendall(b"\r\n")
                    print("SENT Cheese:", self.cheeseChain.stack[id])
                    resp = self.parcingtext(conn)
                    print("RECEIVED: ", resp)
                    conn.close()
                    self.NetworkFlag = True
                except Exception as e:
                    print("Error While Broadcasting: ", e)

        Thread(target=broadcasterThread).start()


if __name__ == "__main__":
    from random import randint
    mem = Client(randint(1000, 8999))
    mem.startclient()
    mem.startListening()

