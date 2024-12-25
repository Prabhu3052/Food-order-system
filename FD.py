import csv

menu = {
    "Pizza": 8.99,
    "Burger": 5.49,
    "Sushi": 12.99,
    "Tacos": 6.99,
    "Salad": 4.99,
    "Sandwich": 5.99,
    "Pasta": 9.49,
    "Fried Chicken": 7.99,
    "Ice Cream": 3.49,
    "Smoothie": 4.99
}

csv_file = "cart.csv"

def initialize_csv():
    try:
        with open(csv_file, mode="x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["item", "quantity"])
    except FileExistsError:
        pass

def add_to_csv(item, quantity):
    cart = read_cart_from_csv()
    if item in cart:
        cart[item] += quantity
    else:
        cart[item] = quantity
    write_cart_to_csv(cart)

def remove_from_csv(item):
    cart = read_cart_from_csv()
    if item in cart:
        del cart[item]
    write_cart_to_csv(cart)

def modify_quantity_in_csv(item, quantity):
    cart = read_cart_from_csv()
    if item in cart:
        cart[item] = quantity
    write_cart_to_csv(cart)

def read_cart_from_csv():
    cart = {}
    try:
        with open(csv_file, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                cart[row["item"]] = int(row["quantity"])
    except FileNotFoundError:
        pass
    return cart

def write_cart_to_csv(cart):
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["item", "quantity"])
        for item, quantity in cart.items():
            writer.writerow([item, quantity])

def display_menu():
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

def add_to_cart(item, quantity):
    if item in menu:
        add_to_csv(item, quantity)
        print(f"{item} added to the cart.")
    else:
        print(f"{item} is not available.")

def remove_from_cart(item):
    cart = read_cart_from_csv()
    if item in cart:
        remove_from_csv(item)
        print(f"{item} removed from the cart.")
    else:
        print(f"{item} is not in the cart.")

def modify_quantity(item, quantity):
    cart = read_cart_from_csv()
    if item in cart:
        modify_quantity_in_csv(item, quantity)
        print(f"{item} quantity updated to {quantity}.")
    else:
        print(f"{item} is not in the cart.")

def view_cart():
    print("\nCart Contents:")
    cart = read_cart_from_csv()
    if cart:
        for item, quantity in cart.items():
            print(f"{item}: {quantity} @ ${menu[item]:.2f} each")
    else:
        print("Your cart is empty.")

def checkout():
    cart = read_cart_from_csv()
    if cart:
        total = sum(menu[item] * quantity for item, quantity in cart.items())
        print(f"\nTotal: ${total:.2f}")
        print("Thank you for your order!")
        write_cart_to_csv({})  # Clear the cart
    else:
        print("Your cart is empty. Nothing to checkout.")

def main():
    initialize_csv()
    while True:
        print("\nOptions: 1. View Menu  2. Add to Cart  3. Remove from Cart  4. Modify Quantity")
        print("         5. View Cart  6. Checkout  7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_menu()
        elif choice == "2":
            item = input("Enter item to add: ").title()
            quantity = int(input("Enter quantity: "))
            add_to_cart(item, quantity)
        elif choice == "3":
            item = input("Enter item to remove: ").title()
            remove_from_cart(item)
        elif choice == "4":
            item = input("Enter item to modify: ").title()
            quantity = int(input("Enter new quantity: "))
            modify_quantity(item, quantity)
        elif choice == "5":
            view_cart()
        elif choice == "6":
            checkout()
        elif choice == "7":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
