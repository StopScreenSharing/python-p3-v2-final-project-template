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
                for i, g in enumerate(gardeners, start=1):
                    print(f"{i}. {g.name} ({g.phone})")
            else:
                print("No gardeners found.")

        elif choice == "2":
            name = input("Enter gardener name: ").strip()
            phone = input("Enter gardener phone number: ").strip()
            try:
                gardener = Gardener.create(name, phone)
                print(f"Gardener added: {gardener}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            gardeners = Gardener.get_all()
            if not gardeners:
                print("No gardeners to update.")
                continue
            for i, g in enumerate(gardeners, start=1):
                print(f"{i}. {g.name} ({g.phone})")
            
            selection = input("Choose a gardener to update: ").strip()
            if not selection.isdigit() or not (1 <= int(selection) <= len(gardeners)):
                print("Invalid selection")
                continue

            gardener = gardeners[int(selection) - 1]

            name = input(f"Enter a new name (leave blank to keep {gardener.name}): ").strip()
            phone = input(f"Enter a new phone number (Leave blank to keep {gardener.phone}): ").strip()

            try: 
                if name:
                    gardener.name = name
                if phone: 
                    gardener.phone = phone
                print(f"Updated gardener {gardener}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "4":
            gardeners = Gardener.get_all()
            if not gardeners:
                print("No gardeners to delete.")
                continue

            for i, g in enumerate(gardeners, start=1):
                print (f"{i}. {g.name} ({g.phone})")
            
            selection = input("Choose a gardener number to delete: ").strip()
            if not selection.isdigit() or not (1 <= int(selection) <= len(gardeners)):
                print("Invalid selection.")
                continue

            gardener = gardeners[int(selection) - 1]
            gardener.delete()
        
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please enter 1-5.")

def plants_menu():
     while True:
         gardeners = Gardener.get_all()
         if not gardeners:
             print("\nNo gardeners yet -- add a gardener first!")
             return
         print("\n🌿 Plants Menu")
         
         for i, g in enumerate(gardeners, starts=1):
             print(f"{i}. {g.name}")
             print(f"{len(gardeners)+1}. Back")

             g_choice = input("Choose a gardener to manage plants: ").strip()
             if not g_choice.isdigit() or not (1 <=(g_choice) <= len(gardeners)+1):
                 print("Invalid selection.")
                 continue
             
             if int(g_choice) == len(gardeners)+1:
                 break
             
             gardener = gardeners[int(g_choice) - 1]

             while True:
                 print(f"\n🌱 Managing plants for {gardener.name}")
                 print("1. View plants")
                 print("2. Add plant")
                 print("3. Update plant")
                 print("4. Delete plant")
                 print("5. Back")
                 



        
        
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
