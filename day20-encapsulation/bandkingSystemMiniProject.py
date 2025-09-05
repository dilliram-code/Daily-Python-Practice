# Mini Project: Mini Banking project

import uuid

class BankAccount:
  def __init__(self, account_holder, balance = 0):
    self.__id_no = str(uuid.uuid4())            # private
    self.__account_holder = account_holder      # private
    self.__balance = balance                    # private
    
  
  @property
  def balance(self):
    return self.__balance
  
  def deposit(self, amount):
    if amount > 0:
      self.__balance = amount
      return True
    return False
  
  def withdraw(self, amount):
    if 0<amount<=self.__balance:
      self.__balance -= amount
      return True
    return False
  
  @staticmethod
  def validate_account_number(account_number):
    return  len(str(account_number)) == 10 and str(account_number).isdigit()
  
  
# create an object
account_holder1 = BankAccount("Shree", 0)


# check initial balance
print("Initial balance:", account_holder1.balance)

# deposite some amount
account_holder1.deposit(3000)

# check after deposit
print("Balance now:", account_holder1.balance)


account_holder1.withdraw(300)
# check after withdrawl
print("Balance after withdrawl:", account_holder1.balance)

# check account validation
print(BankAccount.validate_account_number("1234567890"))

# false input
print(BankAccount.validate_account_number("abc"))

# ==============================Finish============================ #