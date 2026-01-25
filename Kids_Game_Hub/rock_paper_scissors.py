import random

def play():
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    print("\n✊ Rock Paper Scissors ✌️")
    user = input("Choose rock/paper/scissors: ").lower()

    if user not in choices:
        print("Invalid choice")
        return

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
        (user == "paper" and computer == "rock") or \
        (user == "scissors" and computer == "paper"):
        print("🎉 You win!")
    else:
        print("😢 You lose!")
