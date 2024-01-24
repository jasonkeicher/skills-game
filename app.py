import random
import tkinter as tk
from tkinter import messagebox

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
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    messagebox.showinfo("Result", f"User chose {user_choice}, computer chose {computer_choice}\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors")

rock_button = tk.Button(root, text="Rock", command=lambda: play("rock"))
paper_button = tk.Button(root, text="Paper", command=lambda: play("paper"))
scissors_button = tk.Button(root, text="Scissors", command=lambda: play("scissors"))

rock_button.pack()
paper_button.pack()
scissors_button.pack()

root.mainloop()