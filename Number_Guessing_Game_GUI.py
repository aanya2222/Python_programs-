from guizero import App, Text, TextBox, PushButton

import random

class GuessingGame:
    def __init__(self, app):
        self.app = app
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.title = Text(self.app, text="Guessing Game", size=15, color="blue")
        self.instruction = Text(self.app, text="Guess a number between 1 and 100:")
        self.guess_input = TextBox(self.app)
        self.result = Text(self.app, text="")

        self.check_button = PushButton(self.app, text="Check", command=self.check_guess)

    def check_guess(self):
        self.attempts += 1
        guess = int(self.guess_input.value)
        
        if guess < self.secret_number:
            self.result.value = "Try a higher number!"
        elif guess > self.secret_number:
            self.result.value = "Try a lower number!"
        else:
            self.result.value = f"Congratulations! You guessed the number {self.secret_number} in {self.attempts} attempts."
            self.check_button.disable()

# Create an App instance
app = App("Guessing Game", width=300, height=200)

# Create a GuessingGame instance
game = GuessingGame(app)

# Start the GUI event loop
app.display()
