import hashlib

class Cheese:
  HARDNESS = 2

  def __init__(self,id,data,prehash):
    self.id=id
    self.data=data
    self.prehash=prehash
    self.HashMining()

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
    return "[Cheese"+str(self.id)+" "+self.data+"]"


class CheeseChain:

    GENESIS_Cheese = Cheese(0, "god genesis 5000", "0")

    def __init__(self):
        self.stack = [CheeseChain.GENESIS_Cheese]
        
    def createCheese(self, data):
        lastid = self.stack[-1].id
        lasthash = self.stack[-1].hash
        cheese = Cheese(lastid + 1, data, lasthash)
        if self.insertCheese(cheese):
            return cheese
        else:
            return -1
        
    def insertCheese(self, cheese):
        if cheese.hash != cheese.CalculateHash():
            return False
        if not cheese.hash.startswith("0" * cheese.HARDNESS):
            return False
        if cheese.id != self.stack[-1].id + 1:
            return False
        if cheese.prehash != self.stack[-1].hash:
            return False
        self.stack.append(cheese)
        return True
    
    def CheeseID(self, id):
        return self.stack[id]

    def deleteCheese(self):
        self.stack.pop()
        
    def checkCheese(self):
        prehash = CheeseChain.GENESIS_Cheese.hash
        for cheese in self.stack[1:]:
            if cheese.hash != cheese.CalculateHash():
                return False
            if cheese.prehash != prehash:
                return False
            prehash = cheese.hash
        return True

if __name__ == "__main__":
    c = CheeseChain()
    print(c.createCheese("genesis Sri 20"))
    print(c.createCheese("Sri Shamprikta 4"))
    print(c.createCheese("Shamprikta Guillaume 1"))

    print(c)
    c.deleteCheese()
    print(c)
    print(c.checkCheese())
