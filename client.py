import socket
import pickle

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect((socket.gethostname(),1234))

def get_peers():
    message='A|'
    server.send(message)
    while True:
        peer_list=server.recv(1024)
        p=pickle.loads(peerlist)
        print(p)

get_peers()
'''

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