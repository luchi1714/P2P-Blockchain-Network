# 2020-net-b


## About the subject

The main focus of this project concerned implementing a blockchain using a P2P network architecture. Here clients would connect to a tracker which would then send them a ledger containing the last block mined and other clients connected to the network. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. The clients connected would then send the blocks to other clients that are connected to them.

## How to build, run, and test your project
1. Download all files in the repository.

2. In the *tracker.py* file change the `ServerIP` variable to your IP address or whichever computer you desire to be set as the server. In this same file, you can set your desired number of maximum clients by my changing the variable `MaxClient`.

3. Set the IP variable in the *client.py* file to the one of your computer and in this same file change the 'ServerIP' variable to the same IP address that was set in the *tracker.py* file.

4. To run the program you can simply run the *cheesechain.py*, *tracker.py*, *client.py* then the *ClientConsole.py* file.

5.In the GUI enter a port number( it can be any 4 digit number). If testing multiple clients even if it's on the same computer ensure that they have different port numbers.

6. To start mining, directly click on * "Start Client"*. You may click on "Stop client" when you desire to stop.

7.To create a transaction that will be mined into a block enter your account name, transaction ID and an amount the click on the *Make Transaction*.


## interpretation of messages on the client console

* client socket is listening - Joined the tracker successfully and is now waiting for the cheesechain. Initially, the genesis block will be loaded from the file containing pre-existing information. For the purpose of diagnosis "True" will be printed on the 3rd line when the program initially starts running to indicate that other clients have joined the tracker. 

* Recieved: |R| -As mentioned in the protocol R indicated that a block has been received. Initially, the genesis block will be broadcasted and thus this receive message should appear in the UI.

* SENT: *some number * - this indicates how many blocks have been added to the chain.

## Architecture

### Client console

- when the * start client * button  is clicked on in the GUI the `start_clt()` function is executed in the * ClientConsol.py *  file. On the * client.py *  file, this initializes all the cheese and cheese chains.The next function that is called upon clicking this button `clt.startListerning()` , this function points to the `startListening()` function in *client.py* . This function creates a socket and binds itself and starts listening for connections. This function has 2 threads:
    - listenerThread - listens for the `startListerning()`  function
    -  ClientService - Calls the function ClientService to parse the data from other clients. In the `ClientService()` function we also reference the `parcingtext(self,conn)` function which helps us do so. from here the `parcingtext(self,conn)` function reads all the data until "/r" then packages it together to send to other functions. "\n" in this function stops reading this data and moves on to other data. The `ClientService(self,conn)` function gets information from `parcingtext(self,conn)` . In `parcingtext(self,conn)` the reception of a |P| is indicative of a ping request and a |T| is indicative of transmitting a block ie if someone is sending a block. |R| is indicative of a request from another client to send the block.
    
- Making a transaction :
After the necessary information has been entered into this field and the *" Make Transaction"* button is clicked, we pass it into the *client.py* then the *cheesechain.py* file and the function `createCheese(self, data)` is called where the cheese is created. upon reception of the data, we create the `lastid` by incrementing the number of cheese in the chain. In this function, the hash is also calculated and the cheese is created by joining the incremented `lastid`, data and `lasthash`.
After the cheese is created various verifications will be carried out in `insertCheese(self, cheese)` where the hash and id is verified, and `BalanceCheck(self, data)` to verify if the transactor has made a valid transaction ie if the transactor has enough money. It is important to note that in the genesis block we have prebuilt 5000$ received from God (whichever one you believe in, alternatively you could have won a lottery or found the pot of gold at the end of the rainbow, either way, it's your lucky day and you have 5000 whoros in you account :) ) prebuilt.
