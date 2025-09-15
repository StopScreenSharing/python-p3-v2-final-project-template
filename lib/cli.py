# lib/cli.py

from helpers import (
    exit_program,
    main_menu,
    gardener_menu
)


def main():
    while True:
        main_menu()
        choice = input("> ")

        if choice == "0":
            exit_program()
        elif choice == "1":
            gardener_menu()
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
