from expense import Expense
def main():
  print("Running expense tracker!")

  expense = get_user_expense()

  save_expense_to_file()

  summarize_expenses()

def get_user_expense():
  print(f"Getting User Expense!")
  expense_name = input("enter your expense name: ").strip()
  expense_amount = float(input("enter your expense amount: ").strip())
  print(f"Your expense name {expense_name}, {expense_amount}")

  expense_categories = [
    "🍔 Food",
    "🏠 Home",
    "💼 Work",
    "😝 Fun",
    "✨ Misc" 
  ]

  # display the categories
  while True:
    print("select a category:")
    for i, category in enumerate(expense_categories):
      print(f" {i + 1}.{category}")
    value_range = f"[1 - {len(expense_categories)}]"
    selected_index = int(input(f"enter a category number {value_range}:").strip())
    selected_category = expense_categories[selected_index]

    if selected_index in range(1,len(expense_categories)+1):
      new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
      return new_expense
    else:
      print("invalid entry, try again!")
def save_expense_to_file():
  print(f"Saving User Expense!")
  pass

def summarize_expenses():
  print(f"Summarizing User Expense!")
  pass

if __name__ == "__main__":
  main()