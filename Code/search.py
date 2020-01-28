#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # Time Complexity!
    # Best: O(1) - First elemenet
    # Average: O(n) - Have to loop through every element in the array
    # Worst: O(n) - Have to loop through every element in the array
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # Time Complexity!
    # Best: O(1) - First elemenet
    # Average: O(n) - Have to loop through every element in the array
    # Worst: O(n) - Have to loop through every element in the array
    if index > len(array) - 1:
        return None

    if item == array[index]:
        return index

    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    low = 0
    high = len(array)-1
    return binary_search_recursive(array, item, low, high)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # Time Complexity!
    # Best: O(1) - Middle element is the item
    # Average: O(log(n)) - Because we halve the working array every time
    # Worst: O(log(n)) - Even if it is the last possible iteration, it will still be log(n) time
    low = 0
    high = len(array) - 1
    mid = None

    while low <= high:
        mid = (low + high) // 2
        if array[mid] < item:
            low = mid + 1
        elif array[mid] > item:
            high = mid - 1
        else:
            return mid
    return None


def binary_search_recursive(array, item, low, high):
    # Time Complexity!
    # Best: O(1) - Middle element is the item
    # Average: O(log(n)) - Because we halve the working array every time
    # Worst: O(log(n)) - Even if it is the last possible iteration, it will still be log(n) time
    if low > high:
        return None
    mid = (low + high) // 2
    if array[mid] < item:
        return binary_search_recursive(array, item, mid + 1, high)
    elif array[mid] > item:
        return binary_search_recursive(array, item, low, mid - 1)
    else:
        return mid
