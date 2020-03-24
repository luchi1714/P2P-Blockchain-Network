from client import *
import time

'''
How to run

Setup:
1)Select port number
2)Select number of loops in Max_iterations

Run:
Run different instances of TestCheeseChain with different port numbers and with time.sleep() of 30 secounds
we are not saturating the network and blocks are able to transmit


What this test does:
This test makes looping transactions between User1 and User2 for Max_iteration times


'''

port=1114 #Port Number for the client

#Initialising parameters
clt=Client(port)
clt.startListening()
clt.startclient()

#Maximum iterations change as necessary
Max_iterations=200

Genesis="genesis"
TestUserOne="User1"
TestUserTwo="User2"

chese=clt.cheeseChain.createCheese(Genesis+' '+TestUserOne+' '+str(200))
clt.bradcastchain(chese.id)

while True and Max_iterations>0:
    if Max_iterations<0:break
    while Max_iterations>0:
        print("In loop",Max_iterations)
        chese=clt.cheeseChain.createCheese(TestUserOne+' '+TestUserTwo+' '+str(10))
        clt.bradcastchain(chese.id)
        chese=clt.cheeseChain.createCheese(TestUserTwo+' '+TestUserOne+' '+str(10))
        clt.bradcastchain(chese.id)
        Max_iterations-=1
        time.sleep(12)

print(clt.cheeseChain)