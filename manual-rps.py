import random

class RPS:

    def __init__(self):
        self.choices = ["Rock", "Paper", "Scissors"]
        self.computer_score = 0
        self.user_score = 0

    def get_computer_choice(self):
        computer_choice = random.choice(self.choices)
        return computer_choice

    def get_user_choice(self):
        user_choice = input(f"Please pick: {self.choices} ")
        return user_choice
    
    def get_winner(self, computer_choice, user_choice):
        if computer_choice == user_choice:
            self.winner = "Noone"
        elif [computer_choice, user_choice] in [["Rock", "paper"], ["Paper", "Scissors"], ["Scissors", "Rock"]]:
            self.winner = "User"
            self.user_score += 1
        else:
            self.winner = "Computer"
            self.computer_score +=1
        return self.winner

def play_game():
    game = RPS()
    while True:
        computer_choice = game.get_computer_choice()
        user_choice = game.get_user_choice()
        game.get_winner(computer_choice, user_choice)
        print(computer_choice)
        print(user_choice)
        print(game.winner)

if __name__ == '__main__':
    play_game()