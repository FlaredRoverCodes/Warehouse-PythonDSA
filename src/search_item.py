def search_item(inventory, x):
    sorted_inventory = sorted(inventory)

    for i in range(len(sorted_inventory)):
        if sorted_inventory[i] == x:
            return i

    return -1
