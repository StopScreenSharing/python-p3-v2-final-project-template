# lib/helpers.py

from models.gardener import Gardener
from models.plant import Plant

def main_menu():
    print("\n🌱 Gardening Business Manager 🌱")
    print("0. Exit")
    print("1. Manage Gardeners")

def gardener_menu():
    while True:
        print("\n🧑‍🌾 Gardener Menu")
        print("1. View all gardeners")
        print("2. Add a gardener")
        print("3. Update a gardener")
        print("4. Delete a gardener")
        print("5. Back")

        choice = input("> ").strip()

        if choice == "1":
            gardeners = Gardener.get_all()
            if gardeners:
                for g in gardeners:
                    print(g)
            else:
                print("No gardeners found.")

def plants_menu():
     print("\n🌸 Plant Menu")
     print("1. View all plants")
     print("2. Add a plant")
     print("3. Delete a plant")
     print("4. Find plany by species")
     print("5. Back")


def exit_program():
    print("Goodbye!")
    exit()

def pause():
     input("\nPress Enter to Continue...")
