def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order
customer1 = add_item("Tea")
customer1 = add_item("Vada", customer1)
customer2 = add_item("Coffee")
customer2 = add_item("Biscuit", customer2)
customer3 = add_item("Juice")
customer3 = add_item("Sandwich", customer3)
print("Customer 1:", customer1)
print("Customer 2:", customer2)
print("Customer 3:", customer3)
