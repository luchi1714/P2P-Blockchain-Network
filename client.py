
from cheesechain import CheeseChain
from socket import socket, create_connection, gethostname, gethostbyname_ex
from threading import Thread, Timer
import pickle
import os
import time

ServerIP = "172.18.250.104"
ServerPort=9876

IP = "172.18.250.104"

JoinNetworkProtocol="|J|"
RequestClientProtocol="|C|"
PingProtocol="|P|"
TransmitCheese="|T|"
RecieveCheese="|R|"


class Client:
    CHAIN_PATH = str(os.path.expanduser("~")) + "/.chain/"
    os.makedirs(CHAIN_PATH, exist_ok=True)

    def __init__(self, port=1112):
        self.path = Client.CHAIN_PATH + str(port)
        self.port = port
        self.ClientList = []
        self.NetworkFlag = False
        self.cheeseChain = self.Loadchainfromlocal()


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

    def startclient(self):
        self.Loopflag = True
        def runningclient():
            self.JoinNetwork()
            while True and self.Loopflag:
                Thread(target=self.StoreCheese).start()
                Thread(target=self.getblockchain).start()
                time.sleep(30)
        Thread(target=runningclient).start()

    def stopclient(self):
        self.Loopflag = False

    def Loadchainfromlocal(self):
        try:
            return pickle.load(open(self.path, "rb"))
        except:
            return CheeseChain()

    def StoreCheese(self):
        pickle.dump(self.cheeseChain, open(self.path, "wb"))

    def JoinNetwork(self):
        try:
            conn = create_connection((ServerIP, ServerPort))
            conn.sendall(b'|J|\r\n')  # TODO: send network ip?
            conn.sendall(bytes(str(self.port) + '\r\n', 'utf-8'))
            conn.close()
            self.NetworkFlag = True
        except Exception as e:
            print("Error Client Joining the Network: ", e)

    def get_peers(self):
        try:
            conn = create_connection((ServerIP, ServerPort))
            conn.sendall(b"|C|\r\n")
            print("SENT: Get Peer Request")
            self.ClientList = []
            while True:
                l = self.parcingtext(conn)
                if l == "END":
                    break
                else:
                    if (l == IP + ':' + str(self.port)):
                        print((l == IP + ':' + str(self.port)))
                        print("from server client list", l)
                        continue
                    self.ClientList.append(l)
            print("Received Clients: ", self.ClientList)

        except Exception as e:
            print("Error While receiving Client List: ", e)

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

    def ClientService(self, conn):
        l = self.parcingtext(conn)
        print("RECIEVED: ", l)

        if l == "|P|":
            conn.sendall(b"OK\r\n")
            print("SENT: OK")

        if l == "|T|":
            blkdump = self.parcingtext(conn)
            blk = pickle.loads(blkdump)
            print("RECEIVED Cheese: ", blk)
            if len(self.cheeseChain.stack) != blk.id:
                print("SENT: DROP Command")
                conn.sendall(b"DROP\r\n")
            else:
                status = self.cheeseChain.insertCheese(blk)
                if status:
                    print("SENT: OK Command")
                    conn.sendall(b"OK\r\n")
                else:
                    print("SENT: INVALID Command")
                    conn.sendall(b"INVALID\r\n")

        if l == "|R|":
            id = self.parcingtext(conn)
            id = int(id)
            print("RECIEVED: ", id)
            if len(self.cheeseChain.stack) > id:
                blkdump = pickle.dumps(self.cheeseChain.stack[id])
                conn.sendall(blkdump)
                conn.sendall(b"\r\n")
                print("SENT Cheese: ", self.cheeseChain.stack[id])
            else:
                conn.sendall(b"NONE\r\n")
                print("SENT: NONE")

        conn.close()
        print("Connection Closed")

    def getblockchain(self):
        self.get_peers()
        for mem in self.ClientList:
            ip, port = mem.split(":")
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
                if resp == "NONE":
                    print("RECIEVED: NONE")
                    continue
                else:
                    blk = pickle.loads(resp)
                    print("RECIEVED Cheese: ", blk)
                    status = self.cheeseChain.insertCheese(blk)
                    if status:
                        print("Cheese added!")
                    else:
                        print("Cheese ignored!")
            except Exception as e:
                print("Error While Searching for Cheeses: ", e)

    def bradcastchain(self, id):
        def broadcasterThread():
            self.get_peers()
            blkdump = pickle.dumps(self.cheeseChain.stack[id])
            for mem in self.ClientList:
                ip, port = mem.split(":")
                try:
                    conn = create_connection((ip, port))
                    conn.sendall(b'|T|\r\n')
                    print("SENT: Cheese")
                    conn.sendall(blkdump)
                    conn.sendall(b"\r\n")
                    print("SENT Cheese:", self.cheeseChain.stack[id])
                    resp = self.parcingtext(conn)
                    print("RECIVED: ", resp)
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
    # mem.cheeseChain.createBlock("new block 1")
    # mem.cheeseChain.createBlock("new block 2")
