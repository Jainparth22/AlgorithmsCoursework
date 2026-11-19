"""Linear Search. Time O(n), Space O(1). Works on unsorted data."""
from typing import List


def linear_search(arr: List[int], target: int) -> int:
    """Return index of first occurrence of target, or -1."""
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1


if __name__ == "__main__":
    assert linear_search([4, 2, 7, 2], 2) == 1
    assert linear_search([4, 2, 7], 9) == -1
    assert linear_search([], 1) == -1
    print("All tests passed!")
