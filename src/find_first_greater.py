def find_first_greater(inventory, x):
    sorted_inventory = sorted(inventory)

    for item in sorted_inventory:
        if item > x:
            return item

    return -1
