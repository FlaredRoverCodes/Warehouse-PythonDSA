def action(inventory):
    print("[0]\tPrint")
    print("[1]\tAdd\n[2]\tRemove\n[3]\tSum\n[4]\tMax\n", end="")
    print("[5]\tMin\n[6]\tCount\n[7]\tSort\n[8]\tSearch\n", end="")
    print("[9]\tRange\n[10]\tFind First Greater\n[11]\tTop N Frequencies\n[12]\tMedian Of Unique\n", end="")
    print("[13]\tKth Largest")

    user_action = int(input("Choose an action to perform: "))

    if user_action == 0:
        query = ('print',)
        # return None
    elif user_action == 1:
        data = int(input("Enter value: "))
        query = ('add', data)
    elif user_action == 2:
        data = int(input("Enter value: "))
        query = ('remove', data)
    elif user_action == 3:
        query = ('sum',)
    elif user_action == 4:
        query = ('max',)
    elif user_action == 5:
        query = ('min',)
    elif user_action == 6:
        data = int(input("Enter value: "))
        query = ('count', data)
    elif user_action == 7:
        query = ('sort',)
    elif user_action == 8:
        data = int(input("Enter value: "))
        query = ('search', data)
    elif user_action == 9:
        low, high = map(int, input("Enter low and high separated by a space: ").split())
        query = ('range_count', low, high)
    elif user_action == 10:
        data = int(input("Enter value: "))
        query =  ('find_first_greater', data)
    elif user_action == 11:
        data = int(input("Enter value: "))
        query = ('top_n_frequencies', data)
    elif user_action == 12:
        query = ('median_unique',)
    elif user_action == 13:
        data = int(input("Enter value: "))
        query = ('kth_largest', data)
    elif user_action == 'print':
        result = list(inventory)
    else:
        result = None
    
    queries = [[query]]
    return queries