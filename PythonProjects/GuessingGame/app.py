from dataclasses import dataclass
import random

@dataclass
class Player:
  name: str
  score: int = 0

class GuessNumberGame:
  total_games_played = 0
  
  def __init__(self, player: Player, max_number: int = 10):
    self.player = player
    self.max_number = max_number
    self.secret_number = random.randint(1, max_number)
    self.attempts = 3
    GuessNumberGame.total_games_played += 1

player1 = Player("Dilli")
game = GuessNumberGame(player1)
print(game.secret_number)