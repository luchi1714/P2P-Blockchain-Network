from cheesechain import CheeseChain
from socket import socket, create_connection, gethostname, gethostbyname_ex
from threading import Thread, Timer
import pickle
import os
import time

ServerIP = "172.18.250.70"
ServerPort=9876

IP = "172.18.250.70"

JoinNetworkProtocol="|J|"
RequestClientProtocol="|C|"
PingProtocol="|P|"
TransmitCheese="|T|"
RecieveCheese="|R|"


from cheesechain import CheeseChain
from socket import socket, create_connection, gethostname, gethostbyname_ex
from threading import Thread, Timer
import pickle
import os
import time

ServerIP = "81.250.246.39"
ServerPort=9876

IP = "81.250.246.39"  # Remember to change this to your own IP address

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
