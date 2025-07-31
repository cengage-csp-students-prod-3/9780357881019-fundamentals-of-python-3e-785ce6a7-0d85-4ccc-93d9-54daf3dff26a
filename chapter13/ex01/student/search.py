"""
File: search.py

Defines functions for sequential search and binary search with a profiler.
"""

def sequentialSearch(sorted_list, target):
    for index, value in enumerate(sorted_list):
        if value == target:
            return index  # Found target, return index
        elif value > target:
            break  # Target can't be later in the list
    return -1  # Target not found


def binarySearch(target, lyst, profiler = None):
    """Returns the position of the target item if found,
    or -1 otherwise."""
    left = 0
    right = len(lyst) - 1
    while left <= right:
        if profiler: profiler.comparison()
        midpoint = (left + right) // 2
        if target == lyst[midpoint]:
            return midpoint
        elif target < lyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1

