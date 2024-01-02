import tkinter as tk
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("300x150")
        self.master.resizable(False, False)

        self.target_number = random.randint(1, 100)
        self.guess_label = tk.Label(self.master, text="Enter your guess:")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self.master)
        self.guess_entry.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

        self.submit_button = tk.Button(self.master, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack()

        self.remaining_attempts = 5

    def check_guess(self):
        user_guess = int(self.guess_entry.get())

        if user_guess == self.target_number:
            self.result_label.config(text="Congratulations! You guessed it!")
            self.submit_button.config(state=tk.DISABLED)
        elif user_guess < self.target_number:
            self.result_label.config(text="Try a higher number.")
        else:
            self.result_label.config(text="Try a lower number.")

        self.remaining_attempts -= 1

        if self.remaining_attempts == 0:
            self.result_label.config(text=f"Game over. The correct number was {self.target_number}.")
            self.submit_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
  