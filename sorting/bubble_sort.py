"""
Bubble Sort
Time:  O(n²) average/worst, O(n) best (already sorted with early exit)
Space: O(1) in-place
Stable: YES

Each pass bubbles the largest unseen element to its correct position.
"""

from typing import List


def bubble_sort(arr: List[int]) -> None:
    """Sort arr in-place using bubble sort."""
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # early exit if already sorted


def bubble_sort_pure(arr: List[int]) -> List[int]:
    """Return a new sorted list (non-mutating version)."""
    result = arr[:]
    bubble_sort(result)
    return result


if __name__ == "__main__":
    # Test 1: general case
    a = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(a)
    assert a == [11, 12, 22, 25, 34, 64, 90], f"Test 1 failed: {a}"

    # Test 2: already sorted
    b = [1, 2, 3, 4, 5]
    bubble_sort(b)
    assert b == [1, 2, 3, 4, 5], f"Test 2 failed: {b}"

    # Test 3: reverse sorted
    c = [5, 4, 3, 2, 1]
    bubble_sort(c)
    assert c == [1, 2, 3, 4, 5], f"Test 3 failed: {c}"

    # Test 4: single element
    d = [42]
    bubble_sort(d)
    assert d == [42], f"Test 4 failed: {d}"

    # Test 5: duplicates
    e = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    bubble_sort(e)
    assert e == sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]), f"Test 5 failed: {e}"

    # Test 6: empty list
    f: List[int] = []
    bubble_sort(f)
    assert f == [], f"Test 6 failed: {f}"

    # Test 7: negatives
    g = [-3, -1, -4, -1, -5]
    bubble_sort(g)
    assert g == [-5, -4, -3, -1, -1], f"Test 7 failed: {g}"

    print("All tests passed!")
