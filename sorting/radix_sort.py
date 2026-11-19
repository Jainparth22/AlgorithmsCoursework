"""LSD Radix Sort (base 10, supports negatives).
Time O(d * (n + b)), Space O(n + b), Stable."""
from typing import List


def _counting_by_digit(arr: List[int], exp: int) -> List[int]:
    out = [0] * len(arr)
    count = [0] * 10
    for x in arr:
        count[(x // exp) % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for x in reversed(arr):
        d = (x // exp) % 10
        count[d] -= 1
        out[count[d]] = x
    return out


def _radix_nonneg(arr: List[int]) -> List[int]:
    if not arr:
        return []
    exp, mx = 1, max(arr)
    while mx // exp > 0:
        arr = _counting_by_digit(arr, exp)
        exp *= 10
    return arr


def radix_sort(arr: List[int]) -> List[int]:
    neg = _radix_nonneg([-x for x in arr if x < 0])
    pos = _radix_nonneg([x for x in arr if x >= 0])
    return [-x for x in reversed(neg)] + pos


if __name__ == "__main__":
    for t in ([170, 45, 75, 90, 802, 24, 2, 66], [], [5], [-3, 12, -100, 0, 7], [9, 9, 1]):
        assert radix_sort(t) == sorted(t), t
    print("All tests passed!")
