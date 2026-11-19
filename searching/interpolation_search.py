"""Interpolation Search (sorted, uniformly distributed input).
Time O(log log n) average, O(n) worst, Space O(1)."""
from typing import List


def interpolation_search(arr: List[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1
    while lo <= hi and arr[lo] <= target <= arr[hi]:
        if arr[hi] == arr[lo]:
            return lo if arr[lo] == target else -1
        pos = lo + (target - arr[lo]) * (hi - lo) // (arr[hi] - arr[lo])
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1


if __name__ == "__main__":
    a = [10, 20, 30, 40, 50, 60, 70]
    assert interpolation_search(a, 50) == 4
    assert interpolation_search(a, 10) == 0
    assert interpolation_search(a, 70) == 6
    assert interpolation_search(a, 35) == -1
    assert interpolation_search([], 1) == -1
    assert interpolation_search([5, 5, 5], 5) in (0, 1, 2)
    print("All tests passed!")
