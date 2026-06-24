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

    bank_name = "Nepal Rastra Bank"

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
            )
    
    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.__balance += amount

        self.transactions.append(
            Transaction("DEPOSIT", amount)
        )

        print(f"Rs.{amount} deposited successfully.")
    
    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.__balance:
            raise ValueError("Insufficient balance.")

        self.__balance -= amount

        self.transactions.append(
            Transaction("WITHDRAW", amount)
        )

        print(f"Rs.{amount} withdrawn successfully.")