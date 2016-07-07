class Account(object):
  def __init__(self,holder,number,balance):
    self.holder = holder
    self.number = number
    self.balance = balance

  def deposit(self,amount):
    self.balance += amount
    return self.balance


  def withdraw(self,amount):
    if(amount > self.balance):
      print "You dont have sufficient funds to perform this transaction"
      return self.balance

    else:
      self.balance -= amount
      return self.balance

  def show_balance(self):
      return self.balance

  def transfer(self,target,amount):
    if(amount > self.balance):
      print "You dont have sufficient funds to perform this transaction"
      return self.balance
    else:
      self.balance -= amount
      target.balance += amount
      return self.balance


