"""Selection Sort. Time O(n^2) all cases, Space O(1), Not stable."""
from typing import List


def selection_sort(arr: List[int]) -> None:
    n = len(arr)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if arr[j] < arr[m]:
                m = j
        arr[i], arr[m] = arr[m], arr[i]


if __name__ == "__main__":
    for t in ([64, 25, 12, 22, 11], [], [1], [3, 1, 3, 2], [-2, -5, 0]):
        a = t[:]
        selection_sort(a)
        assert a == sorted(t), a
    print("All tests passed!")
