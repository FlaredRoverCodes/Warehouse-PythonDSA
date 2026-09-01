def max_item(inventory):
    if len(inventory) == 0:
        return None

    biggest = inventory[0]

    for item in inventory:
        if item > biggest:
            biggest = item

    return biggest
