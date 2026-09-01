from typing import List, Tuple, Union

from add_item import add_item
from remove_item import remove_item
from sum_items import sum_items
from max_item import max_item
from min_item import min_item
from count_item import count_item
from sort_items import sort_items
from search_item import search_item
from range_count import range_count
from find_first_greater import find_first_greater
from top_n_frequencies import top_n_frequencies
from median_unique import median_unique
from kth_largest import kth_largest


def advanced_warehouse_inventory(inventory: List[int], queries: List[List[Tuple[str, int]]]) -> List[List[Union[None, int, List[int]]]]:

    inv = list(inventory)

    all_results = []

    for query in queries:
        query_results = []

        for op in query:
            name = op[0]

            if name == 'add':
                result = add_item(inv, op[1])

            elif name == 'remove':
                result = remove_item(inv, op[1])

            elif name == 'sum':
                result = sum_items(inv)

            elif name == 'max':
                result = max_item(inv)

            elif name == 'min':
                result = min_item(inv)

            elif name == 'count':
                result = count_item(inv, op[1])

            elif name == 'sort':
                result = sort_items(inv)

            elif name == 'search':
                result = search_item(inv, op[1])

            elif name == 'range_count':
                result = range_count(inv, op[1], op[2])

            elif name == 'find_first_greater':
                result = find_first_greater(inv, op[1])

            elif name == 'top_n_frequencies':
                result = top_n_frequencies(inv, op[1])

            elif name == 'median_unique':
                result = median_unique(inv)

            elif name == 'kth_largest':
                result = kth_largest(inv, op[1])

            else:
                result = None

            query_results.append(result)

        all_results.append(query_results)

    return all_results

if __name__ == "__main__":
    inventory = [10, 20, 20, 30, 40, 50]

    queries = [
        [('add', 60), ('sum',), ('max',), ('min',)],
        [('remove', 20), ('count', 20), ('sort',)],
        [('search', 40), ('search', 999)],
        [('range_count', 10, 40), ('find_first_greater', 35)],
        [('add', 40), ('add', 40), ('top_n_frequencies', 2)],
        [('median_unique',), ('kth_largest', 2), ('kth_largest', 100)],
    ]

    results = advanced_warehouse_inventory(inventory, queries)

    for i in range(len(queries)):
        print("Query " + str(i + 1) + ":", queries[i])
        print("Result :", results[i])
        print()
