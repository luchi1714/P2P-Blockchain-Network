# -*- coding: utf-8 -*-
"""CheeseChain

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nmDswc94zUtqGpyGGR6qoyaBeKmw8Hin
"""

import hashlib
import json
from datetime import datetime
from time import time
from uuid import uuid4
from flask import Flask
from flask import jsonify
from pprint import pprint

class Cheese():
  def __init__(self, nonce, arb_content, seq_nb, transaction, prev_essence='', essence=''):
    self.nonce = nonce
    self.arb_content = arb_content
    self.transaction  = transaction
    self.seq_nb = seq_nb
    self.prev_essence = prev_essence
    if (essence == ''):
      self.essence = self.calcEssence()
    else:
      self.essence = essence
  
  #Equivalent in the code Git :
  # arb_content -> tstamp
  # seq_nb -> transactionList
  # essence -> hash
  # prev_essence -> prev_essence

  def calcEssence(self):
    cheese_string = json.dumps(self.__dict__,sort_keys=True).encode()
    return hashlib.sha1(cheese_string).hexdigest()
  def printEssences(self):
    print("prev_essence",self.prev_essence)
    print("essence",self.essence)

class CheeseChain():
  difficulty = 2
  def __init__(self):
    self.chain = []
    self.uncomfirmed_transactions = []

  def createReblochonCheese(self):
    reblochon_Cheese = Cheese(0, [], 0, "0", '')
    reblochon_Cheese.essence = reblochon_Cheese.calcEssence()
    self.chain.append(reblochon_Cheese)

  def last_cheese(self):
    return self.chain[-1]

  def add_cheese(self, cheese, proof):
    previous_essence = self.last_cheese.essence
    if (previous_essence != cheese.prev_essence):
      return False
    if not CheeseChain.is_valid_proof(cheese, proof):
      return False

    cheese.essence = prrof
    self.chain.append(cheese)
    return True

  def proof_of_work(cheese):
    cheese.nonce = 0
    computed_essence = cheese.essence

    while not computed_hash.startswith('0'*CheeseChain.difficulty):
      cheese.nonce +=1
      computed_essence = cheese.essence

    return computed_essence

  def add_new_transaction(self, transaction):
    self.uncomfirmed_transactions.append(transaction)


  
  def is_valid_proof(cls, cheese, cheese_essence):
    return (cheese_essence.startswith('0'*CheeseChain.difficulty) and cheese_essence == cheese.essence)


  def check_chain_validity(cls, chain):
    result = True
    previous_essence = "0"

    for cheese in chain:
      cheese_essence = cheese.essence
      delattr(cheese)

      if not cls.is_valid_proof(cheese, cheese.essence) or \ previous_essence != cheese.prev_essence:
        result = False
        break
      cheese.essence, previous_essence = cheese_essence, cheese_essence
    return result

  def mine(self):
    if not self.uncomfirmed_transactions:
      return False

    last_cheese = self.last_cheese

    new_cheese = cheese(seq_nb = last_cheese.seq_nb +1,
                        transactions = self.uncomfirmed_transactions,
                        arb_content = time.time(),
                        prev_essence = last_cheese.essence,
                        essence)
    prrof = self.proof_of_work(new_cheese)
    self.add_cheese(new_cheese, proof)

    self.uncomfirmed_transactions = []
    return True