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
    
class BankAccount:
    """
    Base class for all bank accounts.
    """

    bank_name = "Nepal National Bank"

    total_accounts = 0

    def __init__(self, account_number, owner_name, initial_balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.__balance = initial_balance
        self.transactions = []

        BankAccount.total_accounts += 1

        if initial_balance > 0:
            self.transactions.append(
                Transaction("OPEN", initial_balance)