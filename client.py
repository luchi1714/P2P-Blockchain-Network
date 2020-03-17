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


HEADERSIZE=10

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

full_msg=''

while True:
    full_msg=''
    new_msg=True
    while True:
        msg=s.recv(1024)
        if new_msg:
            print(f"new message length:{msg[:HEADERSIZE]}")
            msglen=int(msg[:HEADERSIZE])
            new_msg=False

        full_msg+=msg.decode("utf-8")

        if len(full_msg)-HEADERSIZE==msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            new_msg=True
            full_msg=''
    print(full_msg)'''
'''
