# try..except
try:
  x = int(input("Enter the first number:"))
  y = int(input("Enter the second number:"))
  result = x/y
  print(f"Result: {result}")
except ZeroDivisionError:
  print("Error: Cannot divide by zero.")
except ValueError:
  print("Error: Please enter numbers!")

# 