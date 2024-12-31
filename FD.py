import csv
import os
from datetime import datetime


menu = {
    1: {"name": "Pizza", "price": 12.99},
    2: {"name": "Burger", "price": 8.99},
    3: {"name": "Pasta", "price": 10.99},
    4: {"name": "Salad", "price": 6.99},
    5: {"name": "Sushi", "price": 15.99},
    6: {"name": "Tacos", "price": 9.49},
    7: {"name": "Steak", "price": 22.99},
    8: {"name": "Ramen", "price": 13.49},
    9: {"name": "Sandwich", "price": 7.99},
    10: {"name": "Fries", "price": 4.99},
    11: {"name": "Nachos", "price": 11.49},
    12: {"name": "Hot Dog", "price": 5.99},
    13: {"name": "Curry", "price": 14.49},
    14: {"name": "Wings", "price": 12.49}

}
cart = {}
log_file = "food_order_log.csv"


if not os.path.exists(log_file):
    with open(log_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Action", "Details"])


def log_action(action, details):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, action, details])


def display_menu():
    print("Menu:")
    for item_id, item_details in menu.items():
        print(f"{item_id}. {item_details['name']} - ${item_details['price']}")
    log_action("Display Menu", "Displayed the menu")


def add_to_cart(item_id, quantity):
    if item_id in menu:
        if item_id in cart:
            cart[item_id]["quantity"] += quantity
        else:
            cart[item_id] = {"name": menu[item_id]["name"], "price": menu[item_id]["price"], "quantity": quantity}
        print(f"Added {quantity} x {menu[item_id]['name']} to the cart.")
        log_action("Add to Cart", f"Added {quantity} x {menu[item_id]['name']}")
    else:
        print("Invalid item ID.")


def remove_from_cart(item_id):
    if item_id in cart:
        removed_item = cart[item_id]["name"]
        del cart[item_id]
        print(f"Removed item {removed_item} from the cart.")
        log_action("Remove from Cart", f"Removed {removed_item}")
    else:
        print("Item not found in the cart.")


def modify_cart(item_id, new_quantity):
    if item_id in cart:
        cart[item_id]["quantity"] = new_quantity
        print(f"Updated {cart[item_id]['name']} quantity to {new_quantity}.")
        log_action("Modify Cart", f"Updated {cart[item_id]['name']} to quantity {new_quantity}")
    else:
        print("Item not found in the cart.")


def view_cart():
    if not cart:
        print("Your cart is empty.")
        log_action("View Cart", "Cart is empty")
    else:
        print("Cart:")
        details = []
        for item_id, item_details in cart.items():
            print(f"{item_details['name']} - ${item_details['price']} x {item_details['quantity']}")
            details.append(f"{item_details['name']} x {item_details['quantity']}")
        log_action("View Cart", "; ".join(details))


def checkout():
    if not cart:
        print("Cart is empty. Nothing to checkout.")
        log_action("Checkout", "Attempted checkout with an empty cart")
        return

    total = sum(item["price"] * item["quantity"] for item in cart.values())
    print(f"Your total is: ${total:.2f}")
    log_action("Checkout", f"Total: ${total:.2f}")
    cart.clear()
    print("Thank you for your order!")


def ordering_loop():
    while True:
        print("\nOptions:")
        print("1. View Menu")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. Modify Cart")
        print("5. View Cart")
        print("6. Checkout")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_menu()
        elif choice == "2":
            try:
                item_id = int(input("Enter the item ID to add: "))
                quantity = int(input("Enter the quantity: "))
                add_to_cart(item_id, quantity)
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        elif choice == "3":
            try:
                item_id = int(input("Enter the item ID to remove: "))
                remove_from_cart(item_id)
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        elif choice == "4":
            try:
                item_id = int(input("Enter the item ID to modify: "))
                new_quantity = int(input("Enter the new quantity: "))
                modify_cart(item_id, new_quantity)
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        elif choice == "5":
            view_cart()
        elif choice == "6":
            checkout()
        elif choice == "7":
            print("Goodbye!")
            log_action("Exit", "User exited the application")
            break
        else:
            print("Invalid choice. Please try again.")


ordering_loop()