"""Segment Tree (range sum, point update). build O(n), query/update O(log n)."""
from typing import List


class SegmentTree:
    def __init__(self, data: List[int]):
        self.n = len(data)
        self.t = [0] * (2 * self.n)
        self.t[self.n:] = data
        for i in range(self.n - 1, 0, -1):
            self.t[i] = self.t[2 * i] + self.t[2 * i + 1]

    def update(self, i: int, value: int) -> None:
        i += self.n
        self.t[i] = value
        while i > 1:
            i //= 2
            self.t[i] = self.t[2 * i] + self.t[2 * i + 1]

    def query(self, l: int, r: int) -> int:
        """Sum of data[l:r] (half-open)."""
        res, l, r = 0, l + self.n, r + self.n
        while l < r:
            if l & 1:
                res += self.t[l]; l += 1
            if r & 1:
                r -= 1; res += self.t[r]
            l //= 2; r //= 2
        return res


if __name__ == "__main__":
    import random
    data = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(data)
    assert st.query(1, 4) == 15
    assert st.query(0, 6) == 36
    st.update(1, 10)
    data[1] = 10
    assert st.query(1, 4) == 22
    assert st.query(2, 2) == 0
    arr = [random.randint(-50, 50) for _ in range(37)]  # non power-of-two size
    st = SegmentTree(arr)
    for _ in range(200):
        i = random.randrange(len(arr)); v = random.randint(-50, 50)
        arr[i] = v; st.update(i, v)
        l = random.randrange(len(arr) + 1); r = random.randrange(l, len(arr) + 1)
        assert st.query(l, r) == sum(arr[l:r])
    print("All tests passed!")
