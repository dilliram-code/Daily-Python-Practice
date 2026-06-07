'''Game Flow'''
# Ask the user for the starting balance
# Validate the balance
#   Positive number
# Loop (while balance>0)
#   print the current balance
#   Ask the user to bet
#   Validate the bet
#     bet > 0
#     bet > balance
#   Spin reels
#     generate three random symbols
#   Display the reels
#   Calculate the payout
#     If three symbols match, payout = bet x 10
#     If two symbols match, payout = bet x 2
#     Else, payout = 0
#   Recalculate the balance
#     balance += balance + payout - bet
#   If balance < 0
#       print message
#       break
#   Else
#       ask the user if they want to playing continue
#       If not
#             break out of the loop
def get_starting_balance():
  while True:
    try:
      balance = int(input("Enter starting balance: $"))
      if balance <= 0:
        print("Balance must be a positive number.")
      else:
        return balance
    except ValueError:
      print("Please enter a valid number.")
  
def get_bet_amount(balance):
  while True: 
      try: 
        bet = int(input('Enter your bet amount: \n'))
        if bet > balance or bet <= 0:
          print(f"Invalid bet amount. You can bet between $1 and ${balance}")
        else:
          return bet
      except ValueError:
        print('Please enter a valid number for bet amount.')

def main():
  balance = get_starting_balance()

  print('Welcome you in slot machine game!')
  print(f'start playing with the balance {balance}. \n')


  while balance > 0:
    print(f'Your current balance is $ {balance}.')
    
    





if __name__ == "__main__":
  main()