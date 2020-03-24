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

There are two possibilities on connection:
- Client's IP address is obtained directly from the server: in this case the communication carries on as usual. 
- Client's IP address isn't obtained: in this case the tracker must ask the client for an IP address. The client first sends a message with its' IP address and a connection is then opened by the tracker with the given address to verify  its' validity. The stream finally opens with the sent IP address as the main stream (if everything is ok).

Tracker sends the IP address to the newly connected client.

### Peers
If a peer requests a block, the other peer can answer by sending the requested block if it has it. Otherwise, it will send :
```
|b|0000|
```
This means a peer does not have the block requested.

When a peer finished mining, it sends a `b` message to every connected peers with the new block.

### Malicious peers detection

What is considered as malicious:
- Invalid block
- Invalid message

A peer will be disconnected from the other side of the connection.


## Blockchain

Each block will be stored in a separate  file:
```
block_id.blk
```
The `ID` must be replaced by the number of the block.

### Block file
The first line of the file will contain the ID of the block (identical to the one found in the file name).

The second line will contain the sha1 key of the parent block.

Here, we must talk about the data stored, what is going to happen... An entire part will be dedicated.

The line after the data will correspond to the proof of work.

The last line corresponds  to the sha1 key of this file before adding this line ðŸ¤¯.

### Data

Nothing done at the moment.

