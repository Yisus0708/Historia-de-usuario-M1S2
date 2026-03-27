from products import add_product, show_inventory
from statistics import show_statistics

# Shared inventory list used across all functions
inventory = []

# Main menu loop
running = True
while running:
    print("\n--- MENU ---")
    print("1. Add product")
    print("2. Show inventory")
    print("3. Statistics")
    print("4. Exit")

    option = input("Choose an option: ")

    if option == "1":
        add_product(inventory)
    elif option == "2":
        show_inventory(inventory)
    elif option == "3":
        show_statistics(inventory)
    elif option == "4":
        print("Goodbye.")
        running = False
    else:
        print("Invalid option. Try again.")
