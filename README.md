# 2020-net-b

## About the subject 

The main focus of this project concerned implimenting a blockchain using a P2P network archetecture. 
Here clients would connect to a  tracker which would then send them a ledger containing the last block mined and other clients connected to the network. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. The clients connected would then send the blocks to other clients that are connected to them. 



##  How to build, run, and test your project

1. Download all files in the repository . 
2. In the tracker.py file change the  ` ServerIP ` variable to your own IP address or whichever computer you desire to be set as the server. In this same file you can set your desired number of maximum clients by my changing the variable `MaxClient`.
3. Set the `IP` variable in the client.py folder to the one of your computer and in this same file change the 'ServerIP' variable to the the same IP address that was set in the tracker.py file.

4. To run the program you can simply run the cheesechain.py , tracker.py, client.py then the ClientConsole.py file . 
5. In the GUI  enter a port number( it can be any 4 digit number). If testing multiple clients even if it's on the same computer ensur that they have diferent port numbers.

6. To start mining, directly click on "Start Client".  You may click on "Stop client" when you desire to stop.

7. To create a transaction that will be mined into a block enter your account name, transaction ID  and an amount. 








## Architecture 

