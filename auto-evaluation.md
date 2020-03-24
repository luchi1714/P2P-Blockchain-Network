
# Auto Evaluation

### What works 
- Blockchain and mining blocks 
- Clients are able to send the latest Cheese to atmost 5(can be changed in tracker.py) clients instead of it being broadcasting to everyone for scalability . 
- Functional UI
- Addition of clients with unique Port
- Proof of work for verification is functional(embedded in CheeseChain.py)
- Protocol codes eg|O| to indicate delivery works
- Tracker can connect peers and update the active clients.

### What doesnt work
- If a particular client lags behind a point for say 3 Cheeses, there is no contingency in place to update the CheeseChain of the client
- Every client starts mining immediately there is no configuration to switch to a transactor without being a miner the program, so there is no modes only to be a miner or a transactor

## comparision of obtained results to  initial objectives

- Initially we aimed at having a transactor and a miner modes having the choice to switch mid session but that proved tricky
- we also wanted a UI to make things easier for users which we were able to achieve. 
- We were not able to use length constrained which was previously designed in out protocol.


## Time and contribution 

- Guillaume Sacchetti : Cheesechain, Testing, Tracker  (47hrs)
- Sri Kalidindi : Tracker , UI, Handling, Client ( 53hrs)
- Shampkrita Mehereene : Testing , Cheesechain(37hrs )
- Oluchi Ibeneme : Client , Documentation(37 hrs) 


## Good development practise evaluation
- ### Git
For the most part our program is not more than 10 MB in size keeping with the recommendations. 
English was used as the language of expression in every aspect of the process. For the most part 
Descriptive commit messages were used to describe the contribution from each member . Commits were usually made when a significant 
change was made to the code from someone . 
- ### Code
All of the recommendations were followed in this section.

- ## Testing
- we have done unit testing where we created 3 clients manually and checked if it works as mentioned above
- we have also created a TestCheeseChain.py where for 12 seconds creates a Cheese and transmits it, TestCheeseChain.py can be run in multiple instances with different port numbers. we have tested it with 2 instances and it works.
#### How to run Test:
##### Setup:
- Select port number
- Select number of loops in Max_iterations

##### Run:
-Run different instances of TestCheeseChain with different port numbers and with time.sleep() of 30 secounds
we are not saturating the network and blocks are able to transmit

##### What this test does:
-This test makes looping transactions between User1 and User2 for Max_iteration times


'''
