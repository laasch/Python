# loop.py
import random

CHOICES = ["rock", "paper", "scissors"]

while True:
    print("Make your throw")
    user_choice = input("   Type rock, paper, or scissors: ")
    if user_choice in CHOICES:
        computer_choice = random.choice(CHOICES)
        print(
            f"\nYou threw '{user_choice}', the computer threw '{computer_choice}'"
        )
    else:
        print(f"\nYou typed '{user_choice}' which isn't a valid throw")

    again = input("\nWant some more? (y/n): ")
    if again.lower() == "n":
        break

    print()

print("\nGoodbye")
