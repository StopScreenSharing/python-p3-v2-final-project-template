# lib/helpers.py

from models.gardener import Gardener
from models.plant import Plant

def exit_program():
    print("Goodbye! 🌱")
    exit()

def get_choice(prompt, options):
    """
    Repeatedly ask the user for input until they choose a valid option.
    options: list of strings like ["1", "2", "3"]
    """
    while True:
        choice = input(prompt).strip()
        if choice in options:
            return choice
        print("Invalid choice, try again.")

def get_int(prompt):
    """
    Ask for an integer, re-prompt until valid.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

# -------------------- GARDENERS --------------------

def list_gardeners():
    gardeners = Gardener.get_all()
    if not gardeners:
        print("No gardeners found.")
        return []
    print("\nGardeners:")
    for idx, g in enumerate(gardeners, start=1):
        print(f"{idx}. {g.name} (phone: {g.phone})")
    return gardeners

def add_gardener():
    name = input("Enter gardener name: ").strip()
    phone = get_int("Enter phone number (integer): ")
    gardener = Gardener(name, phone)
    gardener.save()
    print(f"Added gardener: {name}")
    return gardener

def update_gardener(gardener):
    print(f"Updating gardener: {gardener.name}")
    gardener.name = input("New name: ").strip() or gardener.name
    gardener.phone = get_int("New phone number (integer): ")
    gardener.save()
    print("Gardener updated.")

def delete_gardener(gardener):
    confirm = input(f"Delete {gardener.name}? (y/n): ").lower()
    if confirm == "y":
        gardener.delete()
        print("Gardener deleted.")

# -------------------- PLANTS --------------------

def list_plants(gardener):
    plants = Plant.find_by_gardener(gardener.id)
    if not plants:
        print("No plants found for this gardener.")
        return []
    print(f"\nPlants for {gardener.name}:")
    for idx, p in enumerate(plants, start=1):
        print(f"{idx}. {p.name} (height: {p.height})")
    return plants

def add_plant(gardener):
    name = input("Enter plant name: ").strip()
    height = get_int("Enter plant height (integer): ")
    plant = Plant(name, height, gardener.id)
    plant.save()
    print(f"Added plant: {name}")
    return plant

def update_plant(plant):
    print(f"Updating plant: {plant.name}")
    plant.name = input("New name: ").strip() or plant.name
    plant.height = get_int("New height (integer): ")
    plant.save()
    print("Plant updated.")

def delete_plant(plant):
    confirm = input(f"Delete {plant.name}? (y/n): ").lower()
    if confirm == "y":
        plant.delete()
        print("Plant deleted.")