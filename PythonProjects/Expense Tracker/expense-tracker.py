from expense import Expense
import calendar
import datetime

def main():
  budget = 2000
  print("Running expense tracker!")
  expense_file_path = "expenses.csv"
  expense = get_user_expense()
  # print(expense)                # debugging line

  save_expense_to_file(expense, expense_file_path)


  summarize_expenses(expense_file_path, budget)

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

def summarize_expenses(expense_file_path, budget):
  print(f"Summarizing User Expense!")
  expenses: list[Expense] = []
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

    amount_by_category = {}
    for expense in expenses:
      key = expense.category
      if key in amount_by_category:
        amount_by_category[key] += expense.amount
      else:
        amount_by_category[key] = expense.amount  
    print("Expenses by category💹")
    for key, amount in amount_by_category.items():
      print(f"    {key}: ${amount}")

    # calculate the total spent in this month
    total_spent = sum([float(x.amount) for x in expenses])
    print(f"You've spent {total_spent} this month!")

    # get the remaining budget
    remaining_budget = budget - total_spent
    print(f"✅ Budget remaining: ${remaining_budget}.")

    # get the current date
    now = datetime.datetime.now()

    # get the number of days in the current month
    days_in_month = calendar.monthrange(now.year, now.month)[1]

    # calculate the remaining number of days in the current month
    remaining_days = days_in_month - now.day
    
    # get the daily budget
    daily_budget = remaining_budget/remaining_days
    print(f"Budget per day: ${daily_budget}")

if __name__ == "__main__":
  main()