import random

def play():
    number = random.randint(1, 10)
    attempts = 3

    print("\n🎯 Guess the Number (1–10)")

    while attempts > 0:
        guess = int(input("Enter your guess: "))

        if guess == number:
            print("🎉 Correct!")
            return
        else:
            attempts -= 1
            print("Wrong!")

    print("😢 You lost!")
