def top_n_frequencies(inventory, n):
    counts = {}
    for item in inventory:
        if item in counts:
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1

    pairs = []
    for item in counts:
        pairs.append([item, counts[item]])

    size = len(pairs)
    for i in range(size):
        for j in range(size - 1 - i):
            item_a, count_a = pairs[j]
            item_b, count_b = pairs[j + 1]

            should_swap = False
            if count_a < count_b:
                should_swap = True
            elif count_a == count_b and item_a > item_b:
                should_swap = True

            if should_swap:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]

    result = []
    for i in range(n):
        if i < len(pairs):
            result.append(pairs[i][0])

    return result
