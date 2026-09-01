def min_item(inventory):
    if len(inventory) == 0:
        return None

    smallest = inventory[0]

    for item in inventory:
        if item < smallest:
            smallest = item

    return smallest
