'''------------------Simple Calculator Project--------------'''

import math

def addition():
    first = float(input("Enter the first number: ").strip())
    second = float(input("Enter the second number: ").strip())
    return first + second

def subtraction():
    first = float(input("Enter the first number: ").strip())
    second = float(input("Enter the second number: ").strip())
    return first - second

def multiplication():
    first = float(input("Enter the first number: ").strip())
    second = float(input("Enter the second number: ").strip())
    return first * second

def division():
    first = float(input("Enter the first number: ").strip())
    second = float(input("Enter the second number: ").strip())
    if second == 0:
        return "Error: Cannot divide by zero"
    return first / second

def square_root():
    num = float(input("Enter the number: ").strip())
    if num < 0:
        return "Error: Cannot take square root of negative number"
    return math.sqrt(num)
    
def main():
    while True:
        action = input('''
Choose the action to perform:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Square root
6. Exit

Your selection: ''').strip()

        if action == '1':
            print("The addition is:", addition())

        elif action == '2':
            print("The subtraction is:", subtraction())

        elif action == '3':
            print("The multiplication is:", multiplication())

        elif action == '4':
            print("The division is:", division())

        elif action == '5':
            print("The square root is:", square_root())

        elif action == '6':
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid input! Please choose a valid option.\n")

# Run the program
main()