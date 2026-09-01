def range_count(inventory, a, b):
    if a <= b:
        low = a
        high = b
    else:
        low = b
        high = a

    total = 0

    for item in inventory:
        if item >= low and item <= high:
            total = total + 1

    return total
