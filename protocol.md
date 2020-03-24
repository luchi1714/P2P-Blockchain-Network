# Protocol

The following is a detailed  description of the protocol used to implement a blockchain in a peer-to-peer environment through means of a tracker.


## Network

### The messages
A message will take the following format :

```
|l|the content of the message you want to send.
```

`|l|` is the header, its size is fixed: 3 bytes.

`l` is a letter that will indicate the expected action to the receiving  side. Example: `p` would be a ping, `b`  for sending a block etc.


|letter|meaning          |structure of the associated message|description|
|------|-----------------|-----------------------------------|-----------|
|J     |Join Network     |example: 127.0.0.1:8000            |The tracker (server) sends a valid IP address to the client. It sends all the known IP addresses to the new client, however each of them are sent in a new message.|
|C     |Client List            |a block (bytes)                    |A block sent by a peer.|
|P     |Ping          |ID                                 |The ID of the block requested by a peer from another peer. The expected answer is a `b`.|
|T     |Transmit Cheese            |Error message                      |The description of an error|
|R     |Receive Cheese      |To be defined                      |Transaction between users. |
|O     |Okay      |To be defined                      |Transaction between users. 
|E     |End
|D     |Drop Cheese
|I     |Invalid Cheese
|N     |None received
### The Tracker

There are one possibility on connection:
- Client's IP addresses are obtained directly from the tracker maximum of 5(as default but can be changed): then client connects to these maximum number of clients . 

Tracker sends the IP address to the newly connected client.

### Peers
If a peer requests a block, the other peer can answer by sending the requested block if it has it. Otherwise, it will send :
```
|T|
```
This means a peer does not have the block requested.

When a peer finished mining, it sends a `b` message to every connected peers with the new block.

### Malicious peers detection

What is considered as malicious:
- Invalid Cheese
- Invalid message

A peer will be disconnected from the other side of the connection.


## Blockchain

whole block chain will be stored in a file:
```
port_number.blk
```
The `port_number` corresponds to the port number of the client.

### Block file
The first part of the file will contain the ID of the block (identical to the one found in the file name).

The second part will contain the data{sender, receiver, amount}

The third part will have previous cheese hash.

The last part will have current cheese hash

### Data

Nothing done at the moment.

