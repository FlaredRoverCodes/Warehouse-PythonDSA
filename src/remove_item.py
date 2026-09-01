def remove_item(inventory, x):
    new_list = []

    for item in inventory:
        if item != x:
            new_list.append(item)

    inventory[:] = new_list
    return None
