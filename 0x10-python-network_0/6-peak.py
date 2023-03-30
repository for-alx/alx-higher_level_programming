#!/usr/bin/python3
"""
    Peak finder
"""
def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using binary search.

    Args:
    list_of_integers (List[int]): List of unsorted integers.

    Returns:
    int: A peak element in the list.
    """
    if len(list_of_integers) == 0:
        return None
    n = len(list_of_integers)
    l, r = 0, n - 1
    while l < r:
        mid = (l + r) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            l = mid + 1
        else:
            r = mid
    return list_of_integers[l]
