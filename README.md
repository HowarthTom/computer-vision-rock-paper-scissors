# Computer vision project (Rock, Paper, Scissors)

> Teachable machine 
- Created a keras model to detect video user input of either Rock, Paper, or Scissors.

> Manual RPS
- Created the code to run a game of rock, paper, scissors, using manual user input.

> Camera RPS
- Replaced the code for the maanual user input with code that utilised the keras model with videocapture input.
- Added a display to the webcam to improve user-friendliness 

## Milestone 1

- Created a github repository and cloned it to the computer vision folder.

## Milestone 2

- Used the online 'Teachable-Machine' resource to create a model that distinguishes between neutral, rock, paper, and scissors. 
- 2,500 sample images were used for each pose to train the model.
- The model will be used in the project to detect user input and predict to a certain degree of accuracy, whether they chose rock, paper, or scissors. 

## Milestone 3

- Created a new conda environment named 'computer_vision'.
- Installed pip and used it to install the relevant packages needed for the project (opencv-python, tensorflow-macos, ipykernel).
- Created a test.py file with the following code to check that the keras model worked correctly using a numpy array.
```python
from keras.models import load_model
import cv2
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    result = np.argmax(prediction)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(result)
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
```
## Milestone 4

- Created a manual-rps.py file to simulate a game without the use of the keras model.
- Added a computer_choice and user_choice method to the RPS class.
```python
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
```
- Added a get_winner method to determine a winner and update the score.
```python
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
```
- Updated the play_game function to cycle through the rounds until a winner is declared.
```python
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
```

## Milestone 5

- Updated the user_choice method to use camera input instead of manual input, which uses the keras model to identify either neutral, rock, paper, or scissors.
```python
def get_prediction(self, prediction):
        predictied_index = np.argmax(prediction)
        choices = ["Neutral", "Rock", "Paper", "Scissors"]
        predicted_choice = choices[predictied_index]
        return predicted_choice
```
```python
def get_user_choice(self):
    while end_time > time.time(): 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)

    cap.release()
    cv2.destroyAllWindows()

    predicted_choice = RPS.get_prediction(self, prediction)
    return predicted_choice
```
- Created a while loop using time.time() to cyclle through the rounds
```python
end_time = time.time() + 5
while end_time > time.time():
```
- Added a get_winner method to determine a winner and end the game after a score of three has been reached.
```python
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
```
```python
def play_game(winning_score = 3):
    game = RPS()
    while True:
        computer_choice = game.get_computer_choice()
        user_choice = game.get_user_choice()
        game.get_winner(computer_choice, user_choice)
        if game.computer_score == winning_score:
            print(f"Bad luck, the computer won after {game.rounds} rounds.")
            break
        elif game.user_score == winning_score:
            print(f"Well done, you won in {game.rounds} rounds.")
            break
```
- Finally, added a display in the video capture frame to indicate the round, score, current keras model prediction, and a countdown timer until the end of the round.
```python
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
```

## Conclusions

- Overall the model works as intended.
- Improvements I would make would be; 
    - Use a custom keras model that has a greater prediction acuracy.
    - Add a pause at the end of each round to display the round winner.
    - Add a pause at the end of the game to display the overall winner.
    - Make this pause indefinite and add an option to quit or play again using a key input. 
    - Resize the video caputre frame, for user convenience, whilst retaining compatibility between the video data and the shape of the numpy array storing it.