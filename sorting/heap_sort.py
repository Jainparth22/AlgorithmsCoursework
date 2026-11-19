"""Heap Sort. Time O(n log n) all cases, Space O(1), Not stable."""
from typing import List


def _sift_down(arr: List[int], i: int, n: int) -> None:
    while True:
        largest, l, r = i, 2 * i + 1, 2 * i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest == i:
            return
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest


def heap_sort(arr: List[int]) -> None:
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):  # build max-heap
        _sift_down(arr, i, n)
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        _sift_down(arr, 0, end)


if __name__ == "__main__":
    for t in ([12, 11, 13, 5, 6, 7], [], [1], [3, 1, 3, 2], [-2, -5, 0]):
        a = t[:]
        heap_sort(a)
        assert a == sorted(t), a
    print("All tests passed!")
