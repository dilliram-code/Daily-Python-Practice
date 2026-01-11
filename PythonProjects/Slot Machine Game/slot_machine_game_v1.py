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
