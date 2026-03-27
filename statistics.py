# Calculate and display total value and number of products
def show_statistics(inventory):
    if len(inventory) == 0:
        print("No products to calculate.")
    else:
        total_value = 0
        total_items = 0
        for product in inventory:
            total_value += product["price"] * product["quantity"]
            total_items += product["quantity"]
        print("Total inventory value:", total_value)
        print("Total number of products:", total_items)
