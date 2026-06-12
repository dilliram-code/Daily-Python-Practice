from dataclasses import dataclass
import random

@dataclass
class Player:
  name: str
  score: int = 0

