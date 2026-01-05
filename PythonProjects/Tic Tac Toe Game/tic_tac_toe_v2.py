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

from termcolor import colored
# define constants
X = 'X'
O = 'O'

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
    print(f' {cell(row[0])} | {cell(row[1])} | {cell(row[2])} ')
  print(line)

# add color to the moves
def cell(mark):
  color = 'red' if mark == X else 'green'
  return colored(mark,color)

# check winner
def check_winner(board):
  # check rows
  for row in board:
    if row[0] == row[1] == row[2] != ' ':
      return True 
  
  # check columns
  for column in range(2):
    if board[0][column] == board[1][column] == board[2][column] != ' ':
      return True
  
  # check diagonals
  if board[0][0] == board[1][1] == board[2][2] or \
  board[0][2] == board[1][1] == board[2][0] != ' ':
    return True
  
  # if no winner
  return False

# check whether the board is full
def check_board(board):
  for row in board:
    if ' ' in row:
      return False
  return True

def get_position(promt):
  while True:
    try:
      position = int(input(promt))
      if position <0 or position >2:
        raise ValueError
      return position
    except ValueError:
      print("invalid input!")

def get_move(current_player):
  print(f"Player {current_player}'s turn.")
  while True:
    row = get_position("enter row(0-2)")
    column = get_position("enter column(0-2)")
    if board[row][column] == ' ':
      board[row][column] = current_player
      break
    print("This spot is already taken.")


def main():
  print_board(board)
  current_player = X
  while True:
    # get the player's move
    get_move(current_player)
    
    # board fill up progress visualization
    print_board(board)

    if check_winner(board):
      print(f"Player {current_player} wins!")
      break

    # check is board is full
    if check_board(board):
      print(f"Board is full.")
      break
    
    # switch the current player
    current_player = O if current_player == X else X

if __name__ == '__main__':
  main()