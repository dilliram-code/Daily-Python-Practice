'''----------------Game Flow--------------'''
# Declare the board
# Print the board
# Current player = 'X'
# Loop
#     Ask the current player for the move
#     Store their mark on the board
#     Print the board
#     Check the winner
#     If we have a winner
#         Print a message
#         Break
#     If the board is full
#         Print a message
#         Break
#     Switch the current player


# declare the board
board = [
  [' ',' ',' '],
  [' ',' ',' '],
  [' ',' ',' ']
]

def print_board(board):
  line = '---+---+---'
  for row in board:
    print(line)
    print(f' {row[0]} | {row[1]} | {row[2]} ')
  print(line)
print_board(board)