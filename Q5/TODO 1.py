def add_item_buggy(item, order=[]):
    order.append(item)
    return order
def add_item(item, order=None):
    # TODO 1 completed
    if order is None:
        order = []
    order.append(item)
    return order
print(add_item_buggy("Tea"), add_item_buggy("Vada"))
print(add_item("Tea"), add_item("Vada"))
print("Defaults:", add_item_buggy.__defaults__)

