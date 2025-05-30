from game import game
from CustomFunctions import clear

import json


def main():
    print("Welcome to Poker!")
    while True:
        print("1. Play Game\n2. Settings\n3. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Enter an integer!")
            input("Press enter to continue...")
            continue

        if choice == 1:
            players = 6

            game(players)

            while True:
                if input("Play Again? ").lower()[0] == "y":
                    ...
                else:
                    break

        elif choice == 2:
            edit_settings()

        elif choice == 3:
            break

        else:
            print("Invalid choice")
            input("Press Enter to continue...")
        clear()

    print("Thank you for playing!")


def edit_settings() -> None:
    settings = json.load(open("settings.json"))

    while True:
        print("---Settings---\n1. Starting Money\n2. Number of Players\n3. Quit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            starting_amount = int(input("Enter starting amount (min 500, default 1000): "))
            if not starting_amount or starting_amount < 500:
                starting_amount = 1000
            settings["StartingMoney"] = starting_amount

        elif choice == 2:
            while True:
                players = input("Enter number of players (Default is 6): ")
                if not players:
                    players = 6
                    break

                try:
                    players = int(players)
                except ValueError:
                    print("Enter an integer!")
                    input("Press enter to continue...")
                    clear()
                    continue

                if 2 <= players <= 12:
                    break
                else:
                    print("Invalid number of players\nEnter a number between 2 and 12.")
                    input("Press enter to continue...")
                    clear()

            settings["Players"] = players

        elif choice == 3:
            break

        else:
            print("Invalid choice. Choose a number between 1 and 3.")
            input("Press enter to continue...")

        clear()
    json.dump(settings, open("settings.json", "w"))


if __name__ == '__main__':
    main()
