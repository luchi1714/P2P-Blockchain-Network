import socket
from socket import *
from threading import Thread
import random
import time

ServerIP='172.18.250.104'
ServerPort=9876
MaxClient=5

class Tracker:
    def __init__(self):
        self.ClientList=[]

    #Function to start tracker an accept all incomming connections
    def StartTracker(self):
        def acceptAll():
            TrackerSocket=socket()
            TrackerSocket.bind((ServerIP,ServerPort))
            TrackerSocket.listen()
            while True:
                conn,addr=TrackerSocket.accept()
                self.Manager(conn,addr[0])
        '''Function to check if a client is active by pinging each client and updating the 
        active list'''
        def CheckClientStatus():
            while True:
                print("Tracker Status: Running")
                for client in self.ClientList:
                    try:
                        ip = client.split(':')[0]
                        port = int(client.split(':')[1])
                        print("Pinging This Client", ip, port)
                        conn = create_connection((ip, port))
                        conn.sendall(b"|P|\r\n")
                        line = self.parcingtext(conn)
                        if line != "|O|":
                            print("Sending a Ping request to:", ip, port, "Encountered a BAD response: ", line)
                        else:
                            print("Sending a Ping request to", ip, port, "Good Ping", line)
                    except:
                        print("Client Timeout", ip, port )
                        #self.ClientList.remove(client)
                time.sleep(60)
        #Two threads for accepting new connections and checking client status
        Thread(target=CheckClientStatus).start()
        Thread(target=acceptAll).start()
    #Function to parse the input commands \r \n represents end of command and \n for end of data
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

    #Function to serve clients on Join Network requests and active client list requests
    def Manager(self,conn,ip):
        def Manage():
            line=self.parcingtext(conn)
            if line=="|J|":
                port=self.parcingtext(conn)
                addr=ip+":"+port
                if addr not in self.ClientList:
                    self.ClientList.append(addr)
                    print("Member added",ip,port)
                    conn.sendall(b"|O|\r\n")

            elif line=="|C|":
                subset = [self.ClientList[i] for i in sorted(random.sample(range(len(self.ClientList)),
                                                                            MaxClient if len(
                                                                                self.ClientList) > MaxClient else len(
                                                                                self.ClientList)))]
                print("Client list is",self.ClientList)
                for i in subset:
                    conn.sendall((i+"\r\n").encode('UTF-8'))
                conn.sendall(b"|E|\r\n")
            else:
                conn.sendall(("BAD" + "\r\n").encode('UTF-8'))
            conn.close()
        Thread(target=Manage).start()

if __name__=="__main__":
    t=Tracker()
    t.StartTracker()

