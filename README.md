# Computer vision project (Rock, Paper, Scissors)

> Teachable machine 

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