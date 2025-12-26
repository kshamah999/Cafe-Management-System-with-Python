import re

name_regex = r'^[A-Z a-z]{2,50}$'

menu = {
    'pizza': 250,
    'cold coffee': 150,
    'sandwich': 200,
    'pasta': 80,
    'maggie': 100,
    'french fries': 50,
    'spring roll': 220,
    'dosa': 120,
    'wrap': 180,
    'cold coco': 190
}

def show_menu():
    print("\n----- Cafe Menu -----")
    for item, price in menu.items():
        print(f"{item.title():<15} ₹{price}")
    print("----------------------\n")

def take_order():
    order = {}
    while True:
        choice = input("Do you want to order (yes/no): ").strip().lower()

        if choice == "no":
            break
        elif choice == "yes":
            item = input("Enter item name: ").strip().lower()

            if item in menu:
                try:
                    qty = int(input("Enter quantity: "))
                    if qty <= 0:
                        print("Quantity must be more than 0.")
                        continue
                    order[item] = order.get(item, 0) + qty
                except ValueError:
                    print("Please enter a valid quantity.")
            else:
                print("❌ Item not found in the menu.")
        else:
            print("Please enter only 'yes' or 'no'.")
    return order

def generate_bill(order):
    print("\n----- Bill -----")
    total = 0
    for item, qty in order.items():
        price = menu[item]
        cost = price * qty
        total += cost
        print(f"{item.title()} x {qty} = ₹{cost}")
    print(f"Total = ₹{total}")
    print("------------------\n")

def main():
    # name validation added
    name = input("Enter your name: ")
    if not re.match(name_regex, name):
        print("Invalid name! Name must contain only letters (2–50 chars).")
        return

    print(f"\nWelcome {name}! Enjoy your meal 😊")

    while True:
        print("\n1. Show Menu")
        print("2. Take Order")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_menu()
        elif choice == "2":
            show_menu()
            order = take_order()
            if order:
                generate_bill(order)
            else:
                print("No items ordered.")
        elif choice == "3":
            print("Thank you for visiting! Come again 😊")
            break
        else:
            print("Invalid choice. Try again.")

# Run program
main()