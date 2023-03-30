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
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]
