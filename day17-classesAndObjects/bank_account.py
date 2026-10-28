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
