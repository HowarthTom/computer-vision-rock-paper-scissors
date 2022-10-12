from turtle import position
from keras.models import load_model
import cv2
import numpy as np
import random
import time

class RPS:

    def __init__(self):
        self.choices = ["Rock", "Paper", "Scissors"]
        self.computer_score = 0
        self.user_score = 0
        self.rounds = 1

    def get_computer_choice(self):
        computer_choice = random.choice(self.choices)
        return computer_choice

    def get_prediction(self, prediction):
        predictied_index = np.argmax(prediction)
        choices = ["Neutral", "Rock", "Paper", "Scissors"]
        predicted_choice = choices[predictied_index]
        return predicted_choice

    def get_user_choice(self):
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        end_time = time.time() + 5
        countdown = 5
        timer = time.time() + 1
        round_indicator = f"Round: {self.rounds}"
        score = f"Player: {self.user_score}   Computer: {self.computer_score}"

        while end_time > time.time(): 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            predicted_choice = RPS.get_prediction(self, prediction)

            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, round_indicator, (50, 80), font, fontScale=2, color=(15, 220, 250), thickness=5)
            cv2.putText(frame, score, (50, 160), font, fontScale=2, color=(15, 220, 250), thickness=5)
            cv2.putText(frame, str(countdown), (50, 340), font, fontScale=3, color=(50, 50, 250), thickness=5)
            if predicted_choice == "Rock":
                cv2.putText(frame, predicted_choice, (50, 240), font, fontScale=2, color=(250, 0, 60), thickness=5)
            elif predicted_choice == "Paper":
                cv2.putText(frame, predicted_choice, (50, 240), font, fontScale=2, color=(180, 250, 0), thickness=5)
            elif predicted_choice == "Scissors":
                cv2.putText(frame, predicted_choice, (50, 240), font, fontScale=2, color=(120, 0, 250), thickness=5)
            else:
                cv2.putText(frame, predicted_choice, (50, 240), font, fontScale=2, color=(250, 250, 250), thickness=5)
            cv2.imshow('frame', frame)

            if time.time() >= timer:
                timer = time.time() + 1
                countdown -= 1

            if cv2.waitKey(1) & 0xFF == ord('q'): # Press 'q' to close the window
                cap.release()
                cv2.destroyAllWindows()

        cap.release()
        cv2.destroyAllWindows()

        return predicted_choice

    def get_winner(self, computer_choice, user_choice):
        if computer_choice == user_choice:
            self.winner = "Noone"
            self.rounds += 1
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
        print(f"You picked {user_choice}")
        print(f"computer picked {computer_choice}")
        if game.computer_score == winning_score:
            print(f"Bad luck, the computer won after {game.rounds} rounds.")
            break
        elif game.user_score == winning_score:
            print(f"Well done, you won after {game.rounds} rounds.")
            break


if __name__ == '__main__':
    play_game()