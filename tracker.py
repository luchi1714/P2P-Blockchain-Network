import socket
import sys
import threading
import time
from queue import Queue
import pickle

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_address = []


# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        s = socket.socket()
        host=socket.gethostname()
        port = 1234

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Handling connection from multiple clients and saving to a list
# Closing previous connections when server.py file is restarted

def accepting_connections():
    for c in all_connections:
        c.close()

    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(1)  # prevents timeout

            all_connections.append(conn)
            all_address.append(address)

            print("Connection has been established :" + address[0])


        except:
            print("Error accepting connections")


# 2nd thread functions - 1) See all the clients 2) Select a client 3) Send commands to the connected client
# Interactive prompt for sending commands
# turtle> list
# 0 Friend-A Port
# 1 Friend-B Port
# 2 Friend-C Port
# turtle> select 1
# 192.168.0.112> dir

# Display all current active connections with client

def list_connections():
    #keys=['sno','ipaddress','portnumber']

    global results
    results= {}

    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' ')) #modify if nothing comes from client
            conn.recv(20480)
        except:
            del all_connections[i]
            del all_address[i]
            continue

        #results = str(i) + "   " + str(all_address[i][0]) + "   " + str(all_address[i][1]) + "\n"
        #results["sno"] = {"ipaddress":str(all_address[i][0]),}
        results.append({i:{"ipaddress":str(all_address[i][0]),"portnumber":str(all_address[i][1])}})

    print(results)


def serve_clients():
    global host
    global port
    global s
    global results
    client_message=s.recv(1024)
    if client_message=='A|':
        d=pickle.dumps(results)
        s.send(d,"utf-8")




# Create worker threads
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do next job that is in the queue (handle connections, send commands)
def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accepting_connections()
            serve_clients()
        if x == 2:
            list_connections() # it should be modified for a time period

        queue.task_done()


def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)

    queue.join()


create_workers()
create_jobs()

################################################################""
#Start working on a new tracker

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
