import random

class RPS:

    def __init__(self):
        self.choices = ["Rock", "Paper", "Scissors"]

    def get_computer_choice(self):
        computer_choice = random.choice(self.choices)
        return computer_choice

    def get_user_choice(self):
        user_choice = input(f"Please pick: {self.choices}")
        return user_choice

def play_game():
    game = RPS()
    while True:
        game.get_computer_choice()
        game.get_user_choice()

if __name__ == '__main__':
    play_game()