# retrospective 
___

## Organization of work and technologies 

For the development of this project we used our variation of the Extreame programming approach. This approach seemed apporate for this project because we were a small team where initially most of us had a fairly vauge understanding of the technology or how to impliment it. We tried to adapt the timelines and delivaribles to everyones schedules concerning school work. To curbe the potential unproductivity this may have incured we checked in with each other about every 2 days or so. Overall our timelines and develerables changed a lot but the following is a rough draft. 

- **week 1** : Famalarize with blockchain and share new info and useful information with each other as much as possible
- **week 2-3** : Start coding the blockchain and understand its implimentatino without the P2P, understand P2P
- **week 4-5** : Work on protocol  and understand how to impliment a P2P network on its own.
- **week 6 -7 **: Code the tracker 
- **week 8**: clear doubts on the tracker with lecturer 
- **week 9 - 10** : Make necesary adjustments to the tracker  and fix bugs 
- **week 11** :  work on UI and Testing




## difficulties faced
- Implimenting the tracker. Useful examples  that didnt impliment flask were extreamly hard to come by. 
- Implimenting conurency 

## lessons learned
- Basics of blockchain 
-Understanding of P2P networking 
- Better understanding of Git 

## Possile future updates
- Make the peer also exchange a set of “recent transactions” that are transactions that are not yet written into a block. When mining, the member try to mine a block containing all the current transactions.
-Use asymmetric cryptography to represent accounts (public keys) and to sign money transfers (using the private keys).

- When a member receives a list of other members and tries to connect to them, if a connection problem happens, it can “complain” to the tracker. The tracker can then trigger the “liveliness” test on this peer, leading to a faster cleanup of its members list.

- Instead of hard-coding a lot of information, have a cheese stack descriptor file which lists the content of the ReblochonCheese, the difficulty of the blockchain, etc. This file could also contain the address of the tracker and could be send (for example by email) to new users.

## Things we would have done differently
- Not understimating how challenging the P2P implimentation section would be 
- Made pushes directly to the specified reprository instead of ourown 
