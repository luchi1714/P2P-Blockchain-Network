
# Auto Evaluation

### What works 
- Blockchain and mining blocks 
- Clients are able to send the ledger to other clients instead of it being distributed to everyone for scalability . 
- Functional UI
- Addition of clients with unique Port
- Proof of work for verification is functional 
- Protocol codes eg|O| to indicate delivery works 

### What doesnt work
- If a particular client lags behind there is no contingency to update the CheeseChain of the client
- Longest chain in the sequence not considered 
- Every client starts mining immediately there is no configuration to switch to a transactor without being a miner the program.
- Tracker pings the clients to know whether they are still connected and removes them if not, there is a bug in the program we are still working on this, so for now client pings and records the active clients but doesn't remove if he is not active.

## comparision of obtained results to  initial objectives

- Initially we aimed at having a transactor and a miner having the choice to switch mid session but that proved tricky
- we also wanted a UI to make things easier for users which we were able to received . 
- We were not able to use length constrained which was previously designed in out protocol.


## Time and contribution 

- Guillaume Sacchetti : Cheesechain, Testing, Tracker  (47hrs)
- Sri Kalidindi : Tracker , UI, Handline, Client ( 53hrs)
- Shampkrita Mehereene : Testing , Cheesechain(37hrs )
- Oluchi Ibeneme : Client , Documentation(37 hrs) 


## Good development practise evaluation
- ### Git
For the most part our program is not more than 10 MB in size keeping with the recommendations. 
English was used as the language of expression in every aspect of the process. For the most part 
Descriptive commit messages were used to describe the contribution from each member . Commits were ususally made when a significant 
change was made to the code from someone . 
- ### Code
All of the recommendations were followed in this section.

- ## Testing
- we have done unit testing where we created 3 clients manually and checked if it works as mentioned above
- we have also created a TestCheeseChain.py where for 12 seconds creates a Cheese and transmits it, TestCheeseChain.py can be run in multiple instances with different port numbers. we have tested it with 2 instances and it works.
**TBU on this**
