"""Binary Search (sorted input). Time O(log n), Space O(1)."""
from typing import List


def binary_search(arr: List[int], target: int) -> int:
    """Return an index of target in sorted arr, or -1."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def lower_bound(arr: List[int], target: int) -> int:
    """First index i with arr[i] >= target (len(arr) if none)."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


if __name__ == "__main__":
    a = [1, 3, 5, 7, 9, 11]
    assert binary_search(a, 7) == 3
    assert binary_search(a, 1) == 0
    assert binary_search(a, 11) == 5
    assert binary_search(a, 4) == -1
    assert binary_search([], 4) == -1
    assert lower_bound([1, 2, 2, 2, 3], 2) == 1
    assert lower_bound([1, 2, 3], 10) == 3
    print("All tests passed!")
