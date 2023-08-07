import math

def binary_search(ordered_array, search_value):
    lower_bound = 0
    upper_bound = len(ordered_array) - 1

    while lower_bound <= upper_bound:
        mid_point = math.floor((upper_bound - lower_bound)/2)
        value_at_midpoint = ordered_array[mid_point]
        if search_value == value_at_midpoint:
            return mid_point
        elif search_value < value_at_midpoint:
            upper_bound = mid_point -1
        elif search_value > value_at_midpoint:
            lower_bound = mid_point + 1
