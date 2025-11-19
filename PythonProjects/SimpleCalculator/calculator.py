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
  