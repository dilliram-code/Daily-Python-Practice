# Mini Project: Mini Banking project

import uuid

class BankAccount:
  def __init__(self, account_holder, balance = 0):
    self.__id_no = str(uuid.uuid4())            # private
    self.__account_holder = account_holder      # private
    self.__balance = balance                    # private
    