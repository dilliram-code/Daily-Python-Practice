# try..except
# try:
#   x = int(input("Enter the first number:"))
#   y = int(input("Enter the second number:"))
#   result = x/y
#   print(f"Result: {result}")
# except ZeroDivisionError:
#   print("Error: Cannot divide by zero.")
# except ValueError:
#   print("Error: Please enter numbers!")

# Explanation:
# Code that may fail goes inside the try block.
# except catches specific errors.
# Execution continues after handling the exception.

# Catching multiple exceptions
try:
  firstNumber = int(input("Enter the first number:"))
  secondNumber = int(input("Enter the second number:"))
  result = firstNumber/secondNumber
  print(f"Result: {result}")
except (ZeroDivisionError, ValueError) as e:
  print("Error occurred:",e)

# Using a tuple in except handles multiple exception types.
