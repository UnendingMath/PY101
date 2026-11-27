import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f"==> {message}")

def obtain_user_choice():
    prompt(f"Choose one: {", ".join(VALID_CHOICES)}")
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("Please enter a valid choice.")
        choice = input()
    return choice

def display_winner(user, computer):
    if ((user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or 
        (user == "paper" and computer == "rock")):
        prompt(f"You win! The computer chose {computer}.")
    elif ((user == "rock" and computer == "paper") or
        (user == "scissors" and computer == "rock") or
        (user == "paper" and computer == "scissors")):
        prompt(f"The computer wins! The computer chose {computer}.")
    else:
        prompt(f"You and the computer tied! The computer also chose {computer_choice}.")

def obtain_play_again():
    prompt("Do you want to play again? (y/n)")
    choice = input().strip().lower()
    print(choice)
    while choice[0] != "y" and choice[0] != "n": 
        prompt("Please enter a valid input.")
        choice = input().strip().lower()
    return choice

while True:

    user_choice = obtain_user_choice()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(user_choice, computer_choice)

    another = obtain_play_again()
    if another[0] == "n":
         break 
