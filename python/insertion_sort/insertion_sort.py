def insertion_sort(arr):
    """
    Sorts a list of numbers using the insertion sort algorithm.

    :param arr: List of numbers to be sorted.
    :return: Sorted list of numbers.
    """
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j],  = arr[j], arr[j-1]
            j -= 1
    return arr