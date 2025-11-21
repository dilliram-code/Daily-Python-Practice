def main():
  print("Running expense tracker!")

  get_user_expense()

  save_expense_to_file()

  summarize_expenses()

def get_user_expense():
  print(f"Getting User Expense!")
  expense_name = input("enter your expense name: ").strip()
  expense_amount = float(input("enter your expense amount: ").strip())
  print(f"Your expense name {expense_name}, {expense_amount}")

def save_expense_to_file():
  print(f"Saving User Expense!")
  pass

def summarize_expenses():
  print(f"Summarizing User Expense!")
  pass

if __name__ == "__main__":
  main()