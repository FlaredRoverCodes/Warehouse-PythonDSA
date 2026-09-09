from main import advanced_warehouse_inventory
from action import action
import os
def usercode(inventory):
    
    queries = action(inventory)
    os.system('cls')
    queries = []
    while True:
        query = action(inventory)
        queries.append(query[0])

        results = advanced_warehouse_inventory(inventory, queries)   #pass full history

        print("Query " + str(len(queries)) + ":", queries[-1])
        print("Result :", results[-1])   #only show the newest result
        print()

        again = input("Perform another action? (y/n): ").strip().lower()
        if again != 'y':
            break
    return query
    