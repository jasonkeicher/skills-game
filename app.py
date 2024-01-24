import random
import tkinter as tk
from tkinter import messagebox

# Initialize score counters
wins = 0
losses = 0
ties = 0

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user, computer):
    if user == computer:
        return "Tie"
    elif (user == "rock" and computer == "scissors") or (user == "scissors" and computer == "paper") or (user == "paper" and computer == "rock"):
        return "User wins"
    else:
        return "Computer wins"

def play(user_choice):
    global wins, losses, ties
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    # Update score counters based on result
    if result == "User wins":
        wins += 1
    elif result == "Computer wins":
        losses += 1
    else:
        ties += 1
    messagebox.showinfo("Result", f"User chose {user_choice}, computer chose {computer_choice}\n{result}\nWins: {wins}, Losses: {losses}, Ties: {ties}")

root = tk.Tk()
root.title("Rock Paper Scissors")

rock_button = tk.Button(root, text="Rock", command=lambda: play("rock"))
paper_button = tk.Button(root, text="Paper", command=lambda: play("paper"))
scissors_button = tk.Button(root, text="Scissors", command=lambda: play("scissors"))

rock_button.pack()
paper_button.pack()
scissors_button.pack()

root.mainloop()