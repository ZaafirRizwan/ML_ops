class Wallet:
  def __init__(self, balance):
      self.balance = balance
      
  def setamount(self,balance):
      self.balance = balance
      
      
  def getamount(self,balance):
      return self.balance
    
  def removeamount(self,balance):
      self.balance = 0
