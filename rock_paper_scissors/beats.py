# beats.py
import random

CHOICES = ["rock", "paper", "scissors"]

BEATS = {
    "rock": ["scissors"],
    "paper": ["rock"],
    "scissors": ["paper"],
}

MESSAGES = {
    ("rock", "scissors"): "smashes",
    ("paper", "rock"): "covers",
    ("scissors", "paper"): "cut",
}

def show_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print(f"It's a tie! Both users chose '{user_choice}'")
    elif user_choice not in BEATS.keys():
        print(f"\nYou typed '{user_choice}' which isn't a valid throw")
    else:
        # BEATS[user_choice] is the list of things user_choice wins over
        user_wins = computer_choice in BEATS[user_choice]

        if user_wins:
            verb = MESSAGES[(user_choice, computer_choice)]
            print(
                f"{user_choice.capitalize()} {verb} {computer_choice}, you win!"
            )
        else:
            verb = MESSAGES[(computer_choice, user_choice)]
            print(
                f"{computer_choice.capitalize()} {verb} {user_choice}, you lose!"
            )

while True:
    print("Make your throw")
    user_choice = input("   Type rock, paper, or scissors: ")
    computer_choice = random.choice(CHOICES)
    show_winner(user_choice, computer_choice)

    again = input("\nWant some more? (y/n): ")
    if again.lower() == "n":
        break

    print()

print("\nGoodbye")
