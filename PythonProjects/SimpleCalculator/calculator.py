'''------------------Simple Calculator Project--------------'''

def main():
  import math
  def addition(first, second):
    first = int(input("enter the first number: ").strip())
    second = int(input("enter the second number: ").strip())

    return first+second
  
  def subtraction(first, second):
    first = int(input("enter the first number: ").strip())
    second = int(input("enter the second number: ").strip())
    
    return first - second
  
  def multiplication(first, second):
    first = int(input("enter the first number: ").strip())
    second = int(input("enter the second number: ").strip())

    return first*second
  
  def division(first, second):
    first = int(input("enter the first number: ").strip())
    second = int(input("enter the second number: ").strip())

    return first/second
  
  def square_root(first):
    first = int(input("enter the first number: ").strip())
    if first > 0:
      return math.sqrt(first)
    else:
      return "invalid input"
  
  while True:
    action = print('''
          choose the action to perform:
          1. add
          2. subtract
          3. multiply
          4. divide
          5. square_root
          ''')
    if action == '1':
      result = addition()
      print("The addition is: ", result)
    elif action == "2":
      result = subtraction()
      print("The subtraction is: ", result)
    elif action == '3':
      result = multiplication()
      print("The multiplication is: ", result)
    elif action == '4':
      result = division()
      print("The division is: ", result)
    elif action == '5':
      result = square_root()
      print("The square root is: ", square_root)
    else:
      print("Invalid input")
      break

# if __name__ == "__main__":
#   main()