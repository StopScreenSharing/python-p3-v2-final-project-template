# lib/cli.py

from helpers import (
    main_menu,
    gardener_menu,
    plants_menu,
    exit_program,
)


def main():
    
    while True:
        main_menu()
        choice = input("> ").strip()
        
        if choice == "0":
            exit_program()
        elif choice == "1":
            gardener_menu()
        elif choice == "2":
            plants_menu()
        else:
            print("Invalid choice. Please enter 0, 1, or 2!")
            

if __name__ == "__main__":
    main()

