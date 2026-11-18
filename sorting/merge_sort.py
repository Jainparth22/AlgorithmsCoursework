"""
Merge Sort
Time:  O(n log n) — always (best, average, worst)
Space: O(n) — creates new sublists during merge
Stable: YES

Divide and conquer:
  1. Split list in half recursively until size 0 or 1
  2. Merge two sorted halves back together

Best for: when stability matters, sorting linked lists (can be O(1) space),
          external sort (data doesn't fit in memory).
"""

from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """Return a new sorted list. Original arr is not modified."""
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:   # <= for stability
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]


def merge_sort_inplace(arr: List[int], l: int = 0, r: int = None) -> None:
    """In-place merge sort (modifies arr)."""
    if r is None:
        r = len(arr) - 1
    if l >= r:
        return
    m = (l + r) // 2
    merge_sort_inplace(arr, l, m)
    merge_sort_inplace(arr, m + 1, r)
    # merge arr[l..m] and arr[m+1..r]
    left = arr[l:m+1][:]
    right = arr[m+1:r+1][:]
    i = j = 0; k = l
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]; i += 1
        else:
            arr[k] = right[j]; j += 1
        k += 1
    while i < len(left):  arr[k] = left[i];  i += 1; k += 1
    while j < len(right): arr[k] = right[j]; j += 1; k += 1


if __name__ == "__main__":
    import random

    # Test 1: general
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]

    # Test 2: already sorted
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Test 3: reverse sorted
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # Test 4: empty
    assert merge_sort([]) == []

    # Test 5: single element
    assert merge_sort([42]) == [42]

    # Test 6: duplicates
    assert merge_sort([5, 2, 8, 2, 5, 1]) == [1, 2, 2, 5, 5, 8]

    # Test 7: negatives
    assert merge_sort([-3, -1, -4, -1, -5]) == [-5, -4, -3, -1, -1]

    # Test 8: random large array (compare with built-in sort)
    arr = [random.randint(-1000, 1000) for _ in range(1000)]
    assert merge_sort(arr) == sorted(arr)

    # Test in-place version
    arr2 = [38, 27, 43, 3, 9, 82, 10]
    merge_sort_inplace(arr2)
    assert arr2 == [3, 9, 10, 27, 38, 43, 82]

    print("All tests passed!")
