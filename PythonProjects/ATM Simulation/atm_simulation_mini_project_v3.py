class ATM:
  def __init__(self):
    self.balance = 0

  def check_balance(self):
    return self.balance
  
  def deposit(self, amount):
    if amount <= 0:
      raise ValueError("Deposit amount must be positive.")
    self.balance += amount   

  def withdraw(self, amount):
    if amount <= 0:
      raise ValueError("Withdrawl amount must be positive.")
    if amount > self.balance:
      raise ValueError("Insufficient funds.")
    self.balance = self.balance - amount

def main():
  atm = ATM()
  while True:
    choice = input("choose an option: \n 1.check balance\n 2.deposit amount \n 3.withdraw amount\n 4.exit \n")
    if choice == '1':
      balance = atm.check_balance()
      print(f"Your account balance is ${balance}")
    elif choice == '2':
      while True:
        try:
          amount = float(input(f"Enter the amount to be deposited."))
          atm.deposit(amount)
          print(f"Successfully deposited ${amount}.")
          break
        except ValueError as error:
            print(error)
    elif choice == '3':
      while True:
        try:
          amount = float(input("Enter the amount to withdraw."))
          atm.withdraw(amount)
          print(f"Successfully withdrew ${amount}.")
          break
        except ValueError as error:
          print(error)
    elif choice == '4':
      print('Thank you for using the ATM.')
      break 
    else:
      print("Invalid input. Please try again!")

if __name__ == "__main__":
  main()
