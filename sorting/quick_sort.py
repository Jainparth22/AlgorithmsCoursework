"""Quick Sort (Lomuto partition, random pivot).
Time O(n log n) avg / O(n^2) worst, Space O(log n), Not stable."""
import random
from typing import List, Optional


def quick_sort(arr: List[int], lo: int = 0, hi: Optional[int] = None) -> None:
    if hi is None:
        hi = len(arr) - 1
    while lo < hi:
        p = _partition(arr, lo, hi)
        # recurse into the smaller side to keep stack depth O(log n)
        if p - lo < hi - p:
            quick_sort(arr, lo, p - 1)
            lo = p + 1
        else:
            quick_sort(arr, p + 1, hi)
            hi = p - 1


def _partition(arr: List[int], lo: int, hi: int) -> int:
    r = random.randint(lo, hi)
    arr[r], arr[hi] = arr[hi], arr[r]
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i


if __name__ == "__main__":
    for t in ([10, 7, 8, 9, 1, 5], [], [1], [3, 1, 3, 2], [-2, -5, 0], [5] * 10):
        a = t[:]
        quick_sort(a)
        assert a == sorted(t), a
    big = [random.randint(-1000, 1000) for _ in range(2000)]
    b = big[:]
    quick_sort(b)
    assert b == sorted(big)
    print("All tests passed!")
