class BankAccount:
  def __init__(self, owner: str, initial_balance: float = 0.0):
    self.owner = owner
    self.balance = initial_balance
  
  # Getter for balance
  @property
  def balance(self) -> float:
    """Returns the current account balance."""
    return self._balance