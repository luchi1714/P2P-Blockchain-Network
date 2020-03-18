from cheesechain import CheeseChain
from socket import socket, create_connection, gethostname, gethostbyname_ex
from threading import Thread, Timer
import pickle
import os
import time

ServerIP = "172.18.250.70" #this part needs to be changed to your own IP 
ServerPort=9876 # remember to add this to the UI 

IP = "172.18.250.70" # This part needs to be changed to your own 

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
        
 
    def StartTracker(self):
        def acceptAll():
            TrackerSocket=socket()
            TrackerSocket.bind((ServerIP,ServerPort))
            TrackerSocket.listen()
            while True:
                conn,addr=TrackerSocket.accept()
                self.Manager(conn,addr[0])

        def CheckClientStatus():
            while True:
                print("Tracker status: Running")
                for client in self.ClientList:
                    try:
                        ip = client.split(':')[0]
                        port = int(client.split(':')[1])
                        print("Pinging This Client", ip, port)
                        conn = create_connection((ip, port))
                        conn.sendall(b"|P|\r\n")
                        line = self.parcingtext(conn)
                        if line != "OK":
                            print("Sending a ping request to:", ip, port, "Encountered a bad response: ", l)
                        else:
                            print("Sending a ping request to", ip, port, " good ping", l)
                    except:
                        print("Client Timeout", ip, port )
                        self.ClientList.remove(client)
                time.sleep(60)

        Thread(target=CheckClientStatus).start()
        Thread(target=acceptAll).start()

        
        
