from dataclasses import dataclass
import random

@dataclass
class Player:
  name: str
  score: int = 0

class GuessNumberGame:
  total_games_played = 0
  
  # initial initialization
  def __init__(self, player: Player, max_number: int = 10):
    self.player = player
    self.max_number = max_number
    self.secret_number = random.randint(1, max_number)
    self.attempts = 3
    GuessNumberGame.total_games_played += 1

  # implement gameplay logic
  def play(self):
    print(f"\nWelcome {self.player.name}")
    print(f"Guess a number between 1 and {self.max_number}")
    print(f"You have {self.attempts}.\n")
    
    
    
  # get user guess
  def get_user_guess(self):
    try:
      guess = int(input("Enter your guess: "))
      if self.is_valid_guess(guess, self.max_number):
        return guess 
      else:
        print(f"Please enter a number between 1 to {self.max_number}.")
    except ValueError:
      print("Invalid input. Please enter a number")
  
  # static method
  @staticmethod
  def is_valid_guess(guess, max_number):
    return 1 <= guess <= max_number

  # class method 
  @classmethod
  def show_total_games(cls):
    print(f"Total games played: {cls.total_games_played}")


player1 = Player("Dilli")
game = GuessNumberGame(player1)
print(game.secret_number)