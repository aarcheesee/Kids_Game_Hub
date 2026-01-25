import db_helper
import guess_number
import rock_paper_scissors

player = input("Enter your name: ")
db_helper.add_player(player)

while True:
    print("\n🎮 KIDS GAME HUB 🎮")
    print("1. Guess the Number")
    print("2. Rock Paper Scissors")
    print("3. Exit")

    choice = input("Choose a game: ")

    if choice == "1":
        guess_number.play()
    elif choice == "2":
        rock_paper_scissors.play()
    elif choice == "3":
        print("Thanks for playing 👋")
        break
    else:
        print("Invalid choice, try again")
