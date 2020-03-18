# 2020-net-b

## About the subject 

The main focus of this project concerned implimenting a blockchain using a P2P network archetecture. 
Here clients would connect to a  tracker which would then send them a ledger containing the last block mined and other clients connected to the network. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. The clients connected would then send the blocks to other clients that are connected to them. 



##  How to build, run, and test your project

To build the program simply download all files to the computer.  In the client.py folder change the   ` ServerIP ` variable to your own IP address or whichever computer you desire to be set as the server . Next set the `IP` variable to the one of your computer.  Repeat the same process for the tracker.py file then set the desired number of users  by changing the variable `MaxClient` .
To test the program all these variables can be adjusted including the variable `ServerPort`.
To run the program you can simply run the cheesechain.py , tracker.py, client.py then the ClientConsole.py file . In the UI enter the information asked eg port number  or Account Name etc then click on start client. From here  the client will be able  to start mining . In order to see the cheese chain click on  **Print Cheese Chain** at the top of the UI.  
Alternatively if you want to be a transactor  in addition to the other information mentioned you can add a transaction amount in the apporiate window then click on **Make Transaction**


## Architecture 

