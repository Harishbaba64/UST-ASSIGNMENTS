items = [
    ['Bread', 40],
    ['Cookies', 80],
    ['Butter', 120],
    ['Cheese', 180],
    ['Yoghurt', 60]
]


cart = []

def view_items():
    print("Available Items:")
    for item in items:
        print(f"Name: {item[0]}, Price: {item[1]}")

def add_to_cart():
    item_name = input("Enter the item name: ")
    for item in items:
        if item[0] == item_name:
            quantity = int(input("Enter the quantity: "))
            for cart_item in cart:
                if cart_item[0] == item_name:
                    cart_item[1] += quantity
                    cart_item[3] = cart_item[1] * cart_item[2]
                    print(f"Updated {item_name} quantity to {cart_item[1]}")
                    return
            cart.append([item_name, quantity, item[1], quantity * item[1]])
            print(f"Added {item_name} to the cart.")
            return
    print("Item not found!")

def update_cart():
    item_name = input("Which item to be updated: ")
    for cart_item in cart:
        if cart_item[0] == item_name:
            quantity = int(input("Enter the quantity to be updated: "))
            cart_item[1] = quantity
            cart_item[3] = cart_item[1] * cart_item[2]
            print(f"Updated {item_name} quantity to {quantity}")
            return
    print("Item not found in the cart!")

def delete_from_cart():
    item_name = input("Which item to be removed: ")
    for i in range(len(cart)):
        if cart[i][0] == item_name:
            cart.pop(i)
            print(f"Removed {item_name} from the cart.")
            return
    print("Item not found in the cart!")

def print_bill():
    print("\nCart Summary:")
    print("Name, Quantity, Price, Total")
    total_amount = 0
    for cart_item in cart:
        print(f"{cart_item[0]}, {cart_item[1]}, {cart_item[2]}, {cart_item[3]}")
        total_amount += cart_item[3]
    print(f"Total Amount of Bill: {total_amount}")


while True:
    print("\nWhat do you want to do?")
    print("Enter 1 for viewing the items")
    print("Enter 2 for adding the items in cart")
    print("Enter 3 for updating the items in cart")
    print("Enter 4 for deleting the items in cart")
    print("Enter 5 for printing bill")
    print("Enter 6 to exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        view_items()
    elif choice == 2:
        add_to_cart()
    elif choice == 3:
        update_cart()
    elif choice == 4:
        delete_from_cart()
    elif choice == 5:
        print_bill()
    elif choice == 6:
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice! Please try again.")
