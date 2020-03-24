
import hashlib

class Cheese:
  HARDNESS = 4 #This is the parameter to choose to set difficult is to mine the block

  def __init__(self,id,data,prehash):
    self.id=id
    self.data=data
    self.prehash=prehash
    self.HashMining()

  '''This function is to mine the possinle hash it keeps 
  incrementing nounce and tries if it is the solution with appropriate zeros
  if not it tries again incrementing nounce'''
  def HashMining(self):
    self.nounce=0
    self.hash=""
    while not self.hash.startswith("0"*Cheese.HARDNESS):
      self.nounce+=1
      self.hash=self.CalculateHash()

  def CalculateHash(self):
    encCheese=(str(self.id)+
              str(self.data)+
              str(self.nounce)+
              self.prehash).encode('utf-8')
    return hashlib.sha1(encCheese).hexdigest()

  def __repr__(self):
    return "[Cheese "+str(self.id)+" "+self.data+" "+str(self.hash)+"]"


class CheeseChain:
    #Genesis cheese from zero cheese to geneisis
    GENESIS_Cheese = Cheese(0, "CheeseZero genesis 50000", "0")

    def __init__(self):
        self.stack = [CheeseChain.GENESIS_Cheese]
    '''Function to create cheese append last cheese hash from the stack'''
    def createCheese(self, data):
        lastid = self.stack[-1].id
        lasthash = self.stack[-1].hash
        cheese = Cheese(lastid + 1, data, lasthash)
        if self.insertCheese(cheese):
            return cheese
        else:
            return -1
    '''Function to insert cheese if the following parameters are satisfied 
    if hash is valid - if the hash is correct by decrypting the hash and verifies
    if hash starts with the required number of zeros
    if cheese is the latest one from the stack
    if the prehash is really the hash of the last block
    if the balance of the payer has a block associated with the appropriate balance in the cheese stack'''
    def insertCheese(self, cheese):
        if cheese.hash != cheese.CalculateHash():
            return False
        if not cheese.hash.startswith("0" * cheese.HARDNESS):
            return False
        if cheese.id != self.stack[-1].id + 1:
            return False
        if cheese.prehash != self.stack[-1].hash:
            return False
        if not self.BalanceCheck(cheese.data):
            print("check balance error!")
            return False
        self.stack.append(cheese)
        return True

    #Function which returns cheese by id
    def CheeseID(self, id):
        return self.stack[id]

    #Fucntion to delete cheese
    def deleteCheese(self):
        self.stack.pop()

    #Function first cheese for troubleshooting purpose
    def checkCheese(self):
        prehash = CheeseChain.GENESIS_Cheese.hash
        for cheese in self.stack[1:]:
            if cheese.hash != cheese.CalculateHash():
                return False
            if cheese.prehash != prehash:
                return False
            prehash = cheese.hash
        return True


    def __repr__(self):
        rp = "[CheeseChain"
        for b in self.stack:
            rp += " " + str(b)
        return rp + "]"

    #This function goes through all the cheeses and verifies if the payer has the enough balance from the cheeses in the stack
    def BalanceCheck(self, data):
        AccountName = data.split()[0]
        transactionAmount = int(data.split()[2])
        CurrentBalance = 0
        for b in self.stack:
            # transfer to the client
            if b.data.split()[1] == AccountName:
                CurrentBalance = CurrentBalance + int(b.data.split()[2])
            # transfer from the client
            if b.data.split()[0] == AccountName:
                CurrentBalance = CurrentBalance - int(b.data.split()[2])
        return transactionAmount <= CurrentBalance


if __name__ == "__main__":
    c = CheeseChain()
    print(c.createCheese("genesis Sri 20"))
    print(c.createCheese("Sri Shamprikta 4"))
    print(c.createCheese("Shamprikta Guillaume 1"))