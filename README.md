# 2020-net-b


## About the subject

The main focus of this project concerned implementing a blockchain using a P2P network architecture. Here clients would connect to a tracker which would then send them a list of clients connected to the network. In our block chain each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. The clients connected would then send the blocks to other clients that are connected to them.

## How to build, run, and test your project

### How to Build and run
1. Download all files in the repository.

2. In the *tracker.py* file change the `ServerIP` variable to your IP address or whichever computer you desire to be set as the server. In this same file, you can set your desired number of maximum clients by my changing the variable `MaxClien` this is the maximum number of clients shared from tracker to client not a constrained on how many clients that can be connected.

3. Set the IP variable in the *client.py* file to the one of your computer and in this same file change the 'ServerIP' variable to the same IP address that was set in the *tracker.py* file.

4. To run the program you can simply run the *tracker.py* and run *ClientConsole.py*, If you want to add another client to this network just run another instance of *ClientConsole.py*

5. In the GUI enter a port number( it can be any 4 digit number). If testing multiple clients even if it's on the same computer ensure that they have different port numbers.

6. To start mining, directly click on * "Start Client"*. You may click on "Stop client" when you desire to stop.

7. To create a transaction that will be mined into a block enter your account name, transaction ID and an amount the click on the *Make Transaction*. This will create a Cheese,Mines it and broadcasts to the other clients(Maximum of 5, can be tuned by above parameter(MaxClien) in the *tracker.py*) in the network

8. To view the cheesechain click on *print Cheesechain* at the right top of the UI. 

9. Click on *Stop Client* when you wish to stop mining. 


## interpretation of messages on the client console

* client socket is listening - Joined the tracker successfully and is now waiting for the instructions from tracker and other clients. Initially, the genesis block will be loaded. For the purpose of diagnosis,Please Ignore True as it is for diagnosis purposes

* Recieved: |R| -As mentioned in the protocol R indicated that a block has been received. Initially, the genesis block will be broadcasted and thus this receive message should appear in the UI. and whenever a new transaction is done a new Cheese is created and broadcasted in the other client use will see this |R| sign again

* SENT: *some number * - this indicates the id of the Cheese that is sent.

## Architecture

## Client console

- when the * start client * button  is clicked on in the GUI the `start_clt()` function is executed in the * ClientConsol.py *  file. On the * client.py *  file, this initializes all the cheese and cheese chains.The next function that is called upon clicking this button `clt.startListerning()` , this function points to the `startListening()` function in *client.py* . This function creates a socket and binds itself and starts listening for connections. This function has 2 threads:
    - listenerThread - listens for the `startListerning()`  function
    -  ClientService - Calls the function ClientService to parse the data from other clients. In the `ClientService()` function we also reference the `parcingtext(self,conn)` function which helps us do so. from here the `parcingtext(self,conn)` function reads all the instructions until "\r" then packages it together to send to other functions. "\n" states the end of the meesage. The `ClientService(self,conn)` function gets information from `parcingtext(self,conn)` . In `parcingtext(self,conn)` the reception of a |P| is indicative of a ping request and a |T| is indicative of transmitting a block ie if someone is sending a block. |R| is indicative of a request from another client to send the block.
    
- Making a transaction :
After the necessary information has been entered into this field and the *" Make Transaction"* button is clicked, we pass it into the *client.py* then the *cheesechain.py* file and the function `createCheese(self, data)` is called where the cheese is created. upon reception of the data, we create the `lastid` by incrementing the number of cheese in the chain. In this function, the hash is also calculated and the cheese is created by joining the incremented `lastid`, data and `lasthash`.
After the cheese is created various verifications will be carried out in `insertCheese(self, cheese)` where the hash and id is verified, and `BalanceCheck(self, data)` to verify if the transactor has made a valid transaction ie if the transactor has enough money. It is important to note that in the genesis block we have prebuilt has 5000$ from CheeseZero.
 
 
 - viewing the cheese chain : 
 when the button * Print cheesechain * is clicked, in order to show the cheese chain the function is passed through *client.py* and then to *cheesechain.py* to return information on the chain. each chain starts with chain and followed with cheese *id* and data followed with that 
 
 
 ## Client
 
 
 The client file is has all the functionality to serve all the requests from other clients. In addition to this it also stores the curent blockchain into the local memory every ten seconds through the storecheese thread in the `startclient(self)` function. This same function also implimetns the getblockchain thread every 10 seconds which calls the `getblockchain(self)` from local memory and other clients.  In this function, for every  active client in recieve the latest stack id  and request to connect with them and request the latest block .  The blockchain is accepted if it is more than the one we have, otherwise it is ignored else an error is printed. The blocks are coordinated between clinet through their ID's .Every client has a stack of ID's and it retrieves the topmost ID and compares it with the others onthe network to identify the longest and the longest one is then broadcasted. In summary one thread stores the chain in the local memory and the other gets the chain from the other clients, these two threads run every 10 seconds. 
 
 The client joins the netword by calling the `JoinNetwork(self)` and  sends the letter |J| to the tracker to requests to join the network and get the client list  and the trackers client list is also updated.  in addition to this the client also broadcasts its latest block to other clients with the `bradcastchain(self, id)` function. 
 
 
 
The client also loads an block which may be stored locally with the `Loadchainfromlocal(self)` function. if bugs are incountered during running the program it must be insure that there are no locally stored blocks as they may clash with the new ones being created. the client also 
 
 
 ##  CheeseChain
 
 this is the main block chain portion of the program . This file is responsible for creation of blocks, insertion of blocks into the chain and verification of blocks and transactions. 
 
 
 
 
 
 ## Tracker 
 This part o the program is responsible for accepting clients to the network, sharing the client list of connected peers and  also constanty checks for connected peers in the network. The tracker is also responsible for checking if peers are still connected to the network by sening |P| which is a ping request to peers. If there is no response from a client they are dropped. The tracker also uses a parsing function just like the client because they will have to communicate with each other
 
 
 
 
 
 
 
 
 
