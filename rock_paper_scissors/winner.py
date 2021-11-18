# winner.py
import random

CHOICES = ["rock", "paper", "scissors"]

def show_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print(f"It's a tie! Both users chose '{user_choice}'")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors, you win!")
        else:
            print("Paper covers rock, you lose!")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock, you win!")
        else:
            print("Scissors cut paper, you lose!")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cut paper, you win!")
        else:
            print("Rock smashes scissors, you lose!")
    else:
        print(f"\nYou typed '{user_choice}' which isn't a valid throw")

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
