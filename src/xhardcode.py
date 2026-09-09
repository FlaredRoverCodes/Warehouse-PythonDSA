from main import advanced_warehouse_inventory

def hardcode(inventory):
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

    