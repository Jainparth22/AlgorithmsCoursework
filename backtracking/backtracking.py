"""Backtracking: N-Queens, Sudoku solver, Subset Sum."""
from typing import List, Optional


def n_queens(n: int) -> List[List[str]]:
    """All distinct solutions as board rows."""
    cols, d1, d2 = set(), set(), set()
    pos: List[int] = []
    out: List[List[str]] = []

    def place(r: int) -> None:
        if r == n:
            out.append(["." * c + "Q" + "." * (n - c - 1) for c in pos])
            return
        for c in range(n):
            if c in cols or (r - c) in d1 or (r + c) in d2:
                continue
            cols.add(c); d1.add(r - c); d2.add(r + c); pos.append(c)
            place(r + 1)
            cols.remove(c); d1.remove(r - c); d2.remove(r + c); pos.pop()

    place(0)
    return out


def solve_sudoku(b: List[List[int]]) -> bool:
    """Solve in place (0 = empty). Returns False if unsolvable."""
    def ok(r: int, c: int, v: int) -> bool:
        if any(b[r][j] == v for j in range(9)) or any(b[i][c] == v for i in range(9)):
            return False
        br, bc = 3 * (r // 3), 3 * (c // 3)
        return all(b[br + i][bc + j] != v for i in range(3) for j in range(3))

    for r in range(9):
        for c in range(9):
            if b[r][c] == 0:
                for v in range(1, 10):
                    if ok(r, c, v):
                        b[r][c] = v
                        if solve_sudoku(b):
                            return True
                        b[r][c] = 0
                return False
    return True


def subset_sum(nums: List[int], target: int) -> Optional[List[int]]:
    """Return one subset (non-negative ints) summing to target, or None."""
    chosen: List[int] = []

    def go(i: int, remaining: int) -> bool:
        if remaining == 0:
            return True
        if i == len(nums) or remaining < 0:
            return False
        chosen.append(nums[i])
        if go(i + 1, remaining - nums[i]):
            return True
        chosen.pop()
        return go(i + 1, remaining)

    return list(chosen) if go(0, target) else None


if __name__ == "__main__":
    assert [len(n_queens(n)) for n in range(1, 9)] == [1, 0, 0, 2, 10, 4, 40, 92]

    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    assert solve_sudoku(puzzle)
    full = set(range(1, 10))
    assert all(set(row) == full for row in puzzle)
    assert all({puzzle[r][c] for r in range(9)} == full for c in range(9))
    assert puzzle[0] == [5, 3, 4, 6, 7, 8, 9, 1, 2]

    s = subset_sum([3, 34, 4, 12, 5, 2], 9)
    assert s is not None and sum(s) == 9
    assert subset_sum([1, 2, 5], 4) is None
    assert subset_sum([], 0) == []
    print("All tests passed!")
