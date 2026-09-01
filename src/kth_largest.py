def kth_largest(inventory, k):
    unique_items = []
    for item in inventory:
        if item not in unique_items:
            unique_items.append(item)

    unique_items.sort(reverse=True)

    if k <= 0 or k > len(unique_items):
        return -1

    return unique_items[k - 1]
