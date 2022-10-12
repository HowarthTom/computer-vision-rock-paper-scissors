import random

class RPS:

    def __init__(self):
        self.choices = ["Rock", "Paper", "Scissors"]
        self.computer_score = 0
        self.user_score = 0
        self.rounds = 0

    def get_computer_choice(self):
        computer_choice = random.choice(self.choices)
        return computer_choice

    def get_user_choice(self):
        user_choice = input(f"Please pick: {self.choices} ")
        return user_choice
    
    def get_winner(self, computer_choice, user_choice):
        if computer_choice == user_choice:
            self.rounds += 1
            self.winner = "Noone"
        elif [user_choice, computer_choice] in [["Paper", "Rock"], ["Scissors", "Paper"], ["Rock", "Scissors"]]:
            self.winner = "You"
            self.user_score += 1
            self.rounds += 1
        else:
            self.winner = "Computer"
            self.computer_score +=1
            self.rounds +=1
        return self.winner

def play_game(winning_score = 3):
    game = RPS()
    while True:
        computer_choice = game.get_computer_choice()
        user_choice = game.get_user_choice()
        game.get_winner(computer_choice, user_choice)
        print(f"You picked: {user_choice}")
        print(f"Computer picked: {computer_choice}")
        print(f"{game.winner} won the round")
        if game.computer_score == winning_score:
            print(f"Bad luck, the computer won after {game.rounds} rounds.")
            break
        elif game.user_score == winning_score:
            print(f"Well done, you won in {game.rounds} rounds.")
            break

if __name__ == '__main__':
    play_game()