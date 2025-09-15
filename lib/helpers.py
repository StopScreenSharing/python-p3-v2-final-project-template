# lib/helpers.py

from models.gardener import Gardener
from models.plant import Plant

def main_menu():
    print("\n🌱 Gardening Business Manager 🌱")
    print("0. Exit")
    print("1. Manage Gardeners")

    def gardener_menu():
        print("\n🧑‍🌾 Gardener Menu")
        print("1. View all gardeners")
        print("2. Add a gardener")
        print("3. Update a gardener")
        print("4. Delete a gardener")
        print("5. Back")
        


def exit_program():
    print("Goodbye!")
    exit()
