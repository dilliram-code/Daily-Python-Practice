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

def main():
  print_board(board)


  current_player = 'X'
  while True:
    print(f"Player {current_player}'s turn.")
    row = int(input("enter row(0-2)"))
    column = int(input("enter column(0-2)"))

    if board[row][column] == ' ':
      board[row][column] = current_player
    else:
      print("This spot is already taken.")
      continue

    print_board(board)


if __name__ == '__main__':
  main()