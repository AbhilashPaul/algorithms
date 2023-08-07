def linear_search(array, search_value):
    array_size = len(array)
    for  i in range(array_size):
        if search_value == array[i]:
            return i
