import socket
from socket import *
from threading import Thread
import random
import time

ServerIP='192.168.0.27'
ServerPort=9876
MaxClient=5

class Tracker:
    def __init__(self):
        self.ClientList=[]

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
                        #self.ClientList.remove(client)
                time.sleep(60)

        Thread(target=CheckClientStatus).start()
        Thread(target=acceptAll).start()
        
    def Manager(self,conn,ip):
        def Manage():
            line=self.parcingtext(conn)
            if line=="|J|":
                port=self.parcingtext(conn)
                addr=ip+":"+port
                if addr not in self.ClientList:
                    self.ClientList.append(addr)
                    print("Member added")
                    conn.sendall(b"OK\r\n")

            elif line=="|C|":
                subset = [self.ClientList[i] for i in sorted(random.sample(range(len(self.ClientList)),
                                                                            MaxClient if len(
                                                                                self.ClientList) > MaxClient else len(
                                                                                self.ClientList)))]
                for i in subset:
                    conn.sendall((i+"\r\n").encode('UTF-8'))
                conn.sendall(b"END\r\n")

            else:
                conn.sendall(("BAD" + "\r\n").encode('UTF-8'))
            conn.close()
        Thread(target=Manage).start()

if __name__=="__main__":
    t=Tracker()
    t.StartTracker()
