# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

# Display categories
def display_categories():
    print("Available categories:")
    for i, category in enumerate(products.keys(), start=1):
        print(f"{i}. {category}")
    
    category_choice = input("Enter the category number you want to explore: ")
    
    if not category_choice.isdigit():  # Non-numeric input
        print("Invalid input. Please enter a valid number.")
        return None
    
    category_index = int(category_choice) - 1
    if category_index not in range(len(products)):  # Invalid category index
        print("Invalid category number. Please try again.")
        return None

    return category_index


# Display products in a selected category
def display_products(products_list):
    print("Products available:")
    for i, (product, price) in enumerate(products_list, start=1):
        print(f"{i}. {product} - ${price}")

# Sort and display products based on price
def display_sorted_products(products_list, sort_order):
    reverse_order = True if sort_order == 'desc' else False
    sorted_products = sorted(products_list, key=lambda x: x[1], reverse=reverse_order)
    for i, (product, price) in enumerate(sorted_products, start=1):
        print(f"{i}. {product} - ${price}")
    return sorted_products

# Add selected products to the shopping cart
def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

# Display the contents of the shopping cart
def display_cart(cart):
    total_cost = 0
    for product, price, quantity in cart:
        print(f"{product} - ${price} x {quantity} = ${price * quantity}")
        total_cost += price * quantity
    print(f"Total cost: ${total_cost}")

# Generate and display a receipt for the user
def generate_receipt(name, email, cart, total_cost, address):
    print(f"\nReceipt for {name} ({email}):")
    for product, price, quantity in cart:
        print(f"{quantity} x {product} - ${price} = ${price * quantity}")
    print(f"Total Cost: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

# Validate user name to contain first and last name, only alphabets
def validate_name(name):
    if len(name.split()) == 2 and all(part.isalpha() for part in name.split()):
        return True
    return False

# Validate email to contain an @ symbol
def validate_email(email):
    return "@" in email

# Main function where program starts
def main():
    name = input("Enter your name (first and last): ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid first and last name.")
        name = input("Enter your name (first and last): ")

    email = input("Enter your email address: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email address.")
        email = input("Enter your email address: ")

    cart = []
    total_cost = 0

    while True:
        category_index = display_categories()  # Get category index directly from display_categories
        if category_index is None:
            continue  # Loop back to ask for a valid category
        
        selected_category = list(products.keys())[category_index]
        display_products(products[selected_category])
        
        while True:
            user_choice = input("Enter an option: \n1. Select a product to buy\n2. Sort the products by price\n3. Go back to category selection\n4. Finish shopping\n")
            if user_choice == '1':
                product_choice = input("Enter the product number: ")
                if product_choice.isdigit() and int(product_choice) in range(1, len(products[selected_category]) + 1):
                    selected_product = products[selected_category][int(product_choice) - 1]
                    quantity = input("Enter the quantity: ")
                    if quantity.isdigit() and int(quantity) > 0:
                        add_to_cart(cart, selected_product, int(quantity))
                        total_cost += selected_product[1] * int(quantity)
                    else:
                        print("Invalid quantity.")
            elif user_choice == '2':
                sort_order = input("Sort by price: \n1. Ascending\n2. Descending\n")
                sort_order_str = 'asc' if sort_order == '1' else 'desc'
                display_sorted_products(products[selected_category], sort_order_str)
            elif user_choice == '3':
                break  # Go back to category selection
            elif user_choice == '4':
                if cart:
                    print("Your cart: ")
                    display_cart(cart)
                    address = input("Enter your delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something next time.")
                return
            else:
                print("Invalid option. Please try again.")


# Make sure the main function runs when this script is executed
if __name__ == "__main__":
    main()
