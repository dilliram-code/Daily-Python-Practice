class BankAccount:
  def __init__(self, owner: str, initial_balance: float = 0.0):
    self.owner = owner
    self.balance = initial_balance
  
  @property
  def balance(self) -> float:
    """Returns the current account balance."""
    return self._balance

  @balance.setter
  def balance(self, amount: float):
    """Validates and updates the account balance."""
    if amount < 0:
      print(f"Error: Balance cannot be negative. Setting balance for {self.owner} to $0.0.")
      self._balance = 0.0
    else:
      self._balance = float(amount)
  
  def deposit(self, amount: float):
    """Deposits a positive amount into the account."""
    if amount > 0:
      self.balance += amount  # Automatically triggers the getter and setter
      print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
    else:
      print("Error: Deposit amount must be positive.")
  
  def withdraw(self, amount: float):
    """Withdraws money if sufficient balance is available."""
    if amount <= 0:
      print("Error: Withdrawal amount must be positive.")
    elif amount > self.balance:
      print(f"Error: Insufficient funds! Current balance: ${self.balance:.2f}")
    else:
      self.balance -= amount  # Automatically triggers the getter and setter
      print(f"Withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}")

if __name__ == "__main__":
  print("--- Creating Account with Invalid Balance ---")
  account = BankAccount(owner="Alice", initial_balance=-500.0)
  print(f"Current balance for {account.owner}: ${account.balance}\n")

  print("--- Updating Balance Directly ---")
  account.balance = 250.0  # Uses setter
  print(f"Updated balance: ${account.balance}\n")  # Uses getter

  print("--- Attempting Invalid Direct Assignment ---")
  account.balance = -100.0  # Invalid input caught by setter
  print(f"Current balance: ${account.balance}\n")