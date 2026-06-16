from datetime import datetime


class Transaction:
  """
  Represents a single banking transaction
  """
  def __init__(self, transaction_type, amount):
    self.transaction_type = transaction_type
    self.amount = amount
    self.timestamp = datetime.now()
    
  def __str__(self):
    return (
          f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} |"
          f"{self.transaction_type: <12} | Rs.{self.amount}"
    )