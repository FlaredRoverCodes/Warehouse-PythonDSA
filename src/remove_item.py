def remove_item(inventory, x):
    new_list = []

    for item in inventory:
        if item != x:
            new_list.append(item)

    # replace the contents of inventory so the change is kept
    inventory[:] = new_list
    return None
