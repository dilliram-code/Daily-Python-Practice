class ATM:
  def __init__(self):
    self.balance = 0

  def check_balance(self, balance):
    print(f"Your current balance is ${self.balance}.")
  
  def deposit(self, amount):
    if amount > self.balance:
      self.balance += amount
      print(f"Successfully deposited ${amount}.")
    else:
      print(f"Deposit amount must be positive.")
  def withdraw(self, amount):
    if amount > self.balance:
      print(f"Insufficient funds.")
    elif amount < 0:
      print("Withdrawl amount must be positive.")
