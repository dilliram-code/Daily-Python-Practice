'''------------------Simple Calculator Project--------------'''

def main():
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
  