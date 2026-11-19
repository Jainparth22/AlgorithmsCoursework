"""Insertion Sort. Time O(n) best / O(n^2) avg+worst, Space O(1), Stable."""
from typing import List


def insertion_sort(arr: List[int]) -> None:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    for t in ([12, 11, 13, 5, 6], [], [1], [3, 1, 3, 2], [-2, -5, 0], [1, 2, 3]):
        a = t[:]
        insertion_sort(a)
        assert a == sorted(t), a
    print("All tests passed!")
