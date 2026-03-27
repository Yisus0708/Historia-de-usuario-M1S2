# Add a new product to the inventory
def add_product(inventory):
    name = input("Product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    product = {"name": name, "price": price, "quantity": quantity}
    inventory.append(product)
    print("Product added.")

# Show all products in the inventory
def show_inventory(inventory):
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        for product in inventory:
            print("Product:", product["name"], "| Price:", product["price"], "| Quantity:", product["quantity"])
