# simple.py
import random

CHOICES = ["rock", "paper", "scissors"]

print("Make your throw")

user_choice = input("   Type rock, paper, or scissors: ")

if user_choice in CHOICES:
    computer_choice = random.choice(CHOICES)
    print(
        f"\nYou threw '{user_choice}', the computer threw '{computer_choice}'"
    )
else:
    print(f"\nYou typed '{user_choice}' which isn't a valid throw")
