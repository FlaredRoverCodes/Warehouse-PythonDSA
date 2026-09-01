def count_item(inventory, x):
    total = 0

    for item in inventory:
        if item == x:
            total = total + 1

    return total
