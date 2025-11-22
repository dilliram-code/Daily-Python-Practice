from expense import Expense
def main():
  print("Running expense tracker!")
  expense_file_path = "expenses.csv"
  expense = get_user_expense()
  # print(expense)                # debugging line

  save_expense_to_file(expense, expense_file_path)


  summarize_expenses(expense_file_path)

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
    selected_category = expense_categories[selected_index-1]

    if selected_index in range(1,len(expense_categories)+1):
      new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
      return new_expense
    else:
      print("invalid entry, try again!")
def save_expense_to_file(expense: Expense, expense_file_path):
  print(f"Saving User Expense: {expense} to {expense_file_path}")
  with open(expense_file_path, "a") as f:
    f.write(f"{expense.name}, {expense.amount},{expense.category}\n")

def summarize_expenses(expense_file_path):
  print(f"Summarizing User Expense!")
  expenses = []
  with open(expense_file_path, "r") as f:
    lines = f.readlines()
    for line in lines:
      expense_name, expense_amount, expense_category = line.strip().split(",")
      line_expense = Expense(
        name=expense_name,
        amount=expense_amount,
        category=expense_category
        )
      print(line_expense)
      expenses.append(line_expense)
if __name__ == "__main__":
  main()