# lib/cli.py

from models.plant import Plant
from models.gardener import Gardener
from helpers import (
    exit_program, get_choice,
    list_gardeners, add_gardener, update_gardener, delete_gardener,
    list_plants, add_plant, update_plant, delete_plant
)

Gardener.create_table()
Plant.create_Table()

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Manage Gardeners")
        print("2. Exit")

        choice = get_choice("> ", ["1", "2"])
        if choice == "1":
            manage_gardeners()
        elif choice == "2":
            exit_program()

def manage_gardeners():
    while True:
        gardeners = list_gardeners()
        print("\nOptions:")
        print("a. Add Gardener")
        if gardeners:
            print("u. Update Gardener")
            print("d. Delete Gardener")
            print("s. Select Gardener")
        print("b. Back to Main Menu")

        valid_choices = ["a", "b"]
        if gardeners:
            valid_choices += ["u", "d", "s"]

        choice = get_choice("> ", valid_choices)

        if choice == "a":
            add_gardener()
        elif choice == "u":
            gardeners = list_gardeners()
            idx = get_choice("Choose number to update: ", [str(i) for i in range(1, len(gardeners)+1)])
            update_gardener(gardeners[int(idx)-1])
        elif choice == "d":
            gardeners = list_gardeners()
            idx = get_choice("Choose number to delete: ", [str(i) for i in range(1, len(gardeners)+1)])
            delete_gardener(gardeners[int(idx)-1])
        elif choice == "s":
            gardeners = list_gardeners()
            idx = get_choice("Choose number to select: ", [str(i) for i in range(1, len(gardeners)+1)])
            manage_plants(gardeners[int(idx)-1])
        elif choice == "b":
            break

def manage_plants(gardener):
    while True:
        plants = list_plants(gardener)
        print("\nOptions:")
        print("a. Add Plant")
        if plants:
            print("u. Update Plant")
            print("d. Delete Plant")
        print("b. Back to Gardeners")

        valid_choices = ["a", "b"]
        if plants:
            valid_choices += ["u", "d"]

        choice = get_choice("> ", valid_choices)

        if choice == "a":
            add_plant(gardener)
        elif choice == "u":
            plants = list_plants(gardener)
            idx = get_choice("Choose number to update: ", [str(i) for i in range(1, len(plants)+1)])
            update_plant(plants[int(idx)-1])
        elif choice == "d":
            plants = list_plants(gardener)
            idx = get_choice("Choose number to delete: ", [str(i) for i in range(1, len(plants)+1)])
            delete_plant(plants[int(idx)-1])
        elif choice == "b":
            break

if __name__ == "__main__":
    main_menu()
