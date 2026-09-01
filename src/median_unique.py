def median_unique(inventory):
    unique_items = []
    for item in inventory:
        if item not in unique_items:
            unique_items.append(item)

    unique_items.sort()

    size = len(unique_items)
    if size == 0:
        return None

    middle = size // 2

    if size % 2 == 1:
        return unique_items[middle]
    else:
        left_value = unique_items[middle - 1]
        right_value = unique_items[middle]
        median = (left_value + right_value) / 2

        if median == int(median):
            return int(median)
        else:
            return median
