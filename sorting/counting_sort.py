"""Counting Sort (supports negatives). Time O(n + k), Space O(n + k), Stable."""
from typing import List


def counting_sort(arr: List[int]) -> List[int]:
    if not arr:
        return []
    lo, hi = min(arr), max(arr)
    count = [0] * (hi - lo + 1)
    for x in arr:
        count[x - lo] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    out = [0] * len(arr)
    for x in reversed(arr):  # reversed keeps it stable
        count[x - lo] -= 1
        out[count[x - lo]] = x
    return out


if __name__ == "__main__":
    for t in ([4, 2, 2, 8, 3, 3, 1], [], [1], [-3, 5, -3, 0], [7, 7, 7]):
        assert counting_sort(t) == sorted(t), t
    print("All tests passed!")
