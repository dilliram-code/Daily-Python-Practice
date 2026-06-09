import random


class SlotMachine:
    def __init__(self):
        self.symbols = {
            "🍒": {"weight": 30, "multiplier": 2},
            "🍋": {"weight": 25, "multiplier": 3},
            "🔔": {"weight": 20, "multiplier": 5},
            "⭐": {"weight": 15, "multiplier": 8},
            "💎": {"weight": 8, "multiplier": 15},
            "7️⃣": {"weight": 2, "multiplier": 50}
        }

        self.rows = 3
        self.cols = 3
        self.balance = 0

    def get_starting_balance(self):
        while True:
            try:
                balance = int(input("Enter starting balance: $"))
                if balance <= 0:
                    print("Balance must be positive.")
                else:
                    self.balance = balance
                    break
            except ValueError:
                print("Please enter a valid number.")

    def get_bet_amount(self):
        while True:
            try:
                bet = int(input("Enter your bet amount: $"))
                if bet <= 0:
                    print("Bet must be positive.")
                elif bet > self.balance:
                    print("You cannot bet more than your balance.")
                else:
                    return bet
            except ValueError:
                print("Please enter a valid number.")

    def spin(self):
        symbol_list = list(self.symbols.keys())
        weights = [self.symbols[symbol]["weight"] for symbol in symbol_list]

        grid = []

        for _ in range(self.rows):
            row = random.choices(symbol_list, weights=weights, k=self.cols)
            grid.append(row)

        return grid

    def display_grid(self, grid):
        print("\n--- SLOT MACHINE ---")
        for row in grid:
            print(" | ".join(row))
        print("--------------------\n")

    def calculate_payout(self, grid, bet):
        total_payout = 0

        for row in grid:
            if row[0] == row[1] == row[2]:
                symbol = row[0]
                multiplier = self.symbols[symbol]["multiplier"]
                total_payout += bet * multiplier

        for col in range(self.cols):
            if grid[0][col] == grid[1][col] == grid[2][col]:
                symbol = grid[0][col]
                multiplier = self.symbols[symbol]["multiplier"]
                total_payout += bet * multiplier

        if grid[0][0] == grid[1][1] == grid[2][2]:
            symbol = grid[0][0]
            multiplier = self.symbols[symbol]["multiplier"]
            total_payout += bet * multiplier

        if grid[0][2] == grid[1][1] == grid[2][0]:
            symbol = grid[0][2]
            multiplier = self.symbols[symbol]["multiplier"]
            total_payout += bet * multiplier

        return total_payout

    def play_round(self):
        print(f"Current balance: ${self.balance}")

        bet = self.get_bet_amount()

        self.balance -= bet

        grid = self.spin()

        self.display_grid(grid)

        payout = self.calculate_payout(grid, bet)

        if payout > 0:
            print(f"You won ${payout}!")
            self.balance += payout
        else:
            print("You lost this round.")

        print(f"New balance: ${self.balance}\n")

    def start_game(self):
        print("Welcome to the Advanced Slot Machine Game!")

        self.get_starting_balance()

        while self.balance > 0:
            self.play_round()

            if self.balance <= 0:
                print("You are out of money. Game over!")
                break

            choice = input("Do you want to play again? (y/n): ").lower()

            if choice != "y":
                print(f"You left the game with ${self.balance}.")
                break


if __name__ == "__main__":
    game = SlotMachine()
    game.start_game()