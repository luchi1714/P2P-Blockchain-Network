
from cheesechain import CheeseChain
from socket import socket, create_connection, gethostname, gethostbyname_ex
from threading import Thread, Timer
import pickle
import os
import time

ServerIP = "81.250.246.39"
ServerPort=9876

IP = "81.250.246.39"

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
            r=conn.recv(1)
            if len(r)==0:
                return None
            if r==b"\n" and readFlag:
                break
            if readFlag:
                responce+=b"\r";
            if r==b"\r":
                readFlag=True;
            else:
                readFlag=False;
                responce+=r;
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
                    if (l == IP + ':' + str(self.port)):  # ignore self
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

