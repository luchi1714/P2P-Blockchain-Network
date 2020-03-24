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


|letter|Abrevation          |Who sends it     |Who receives it   |Usage      |content of msg    |Meaning                                                            |Format of the message          |
|------|--------------------|-----------------|------------------|-----------|------------------|-------------------------------------------------------------------|-------------------------------|
|J     |Join Network        |Client           |Tracker           |Once       |None              |to join the network                                                |list as ip and port            |
|C     |Client List         |Tracker          |Client            |multiple   |List of clients   |contains list of active clients.                                   |list of clients ip:port        |
|P     |Ping                |Tracker          |Client            |multiple   |\r\n              |to check if a client is active                                     |string                         |
|T     |Transmit Cheese     |Client           |Client            |multiple   |Cheese            |Sending cheese                                                     |python object using pickle     |
|R     |Receive Cheese      |Client           |Client            |multiple   |Cheese            |Receiving cheese                                                   |python object using pickle     |
|O     |Okay                |Tracker,Client   |Tracker,Client    |multiple   |None              |to let if the cheese is okay                                       |string                         |
|E     |End                 |Tracker          |Client            |multiple   |None              |end of the client list                                             |string                         |
|D     |Drop Cheese         |Client           |Client            |multiple   |None              |to let other clients that this client dropped cheese               |string                         |
|I     |Invalid Cheese      |Client           |Client            |multiple   |None              |to let other clients know that we received invalid cheese          |string                         |
|N     |None received       |Client           |Client            |multiple   |None              |a way to tell other clients we dont have what you are looking for  |string                         |
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

