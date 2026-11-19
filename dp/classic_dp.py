"""Classic dynamic programming: 0/1 Knapsack, LCS, LIS, Matrix Chain."""
from bisect import bisect_left
from typing import List


def knapsack(weights: List[int], values: List[int], cap: int) -> int:
    """0/1 knapsack. Time O(n*cap), Space O(cap)."""
    dp = [0] * (cap + 1)
    for w, v in zip(weights, values):
        for c in range(cap, w - 1, -1):  # backwards so each item is used once
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[cap]


def lcs(a: str, b: str) -> str:
    """Longest common subsequence. Time O(n*m)."""
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = dp[i][j] + 1 if a[i] == b[j] else max(dp[i][j + 1], dp[i + 1][j])
    i, j, out = n, m, []
    while i and j:
        if a[i - 1] == b[j - 1]:
            out.append(a[i - 1]); i -= 1; j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(out))


def lis_length(arr: List[int]) -> int:
    """Strictly increasing subsequence length. Time O(n log n)."""
    tails: List[int] = []
    for x in arr:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def matrix_chain(dims: List[int]) -> int:
    """Min scalar multiplications; matrix i is dims[i] x dims[i+1]. Time O(n^3)."""
    n = len(dims) - 1
    if n <= 1:
        return 0
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = min(dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                           for k in range(i, j))
    return dp[0][n - 1]


if __name__ == "__main__":
    assert knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9
    assert knapsack([], [], 10) == 0
    assert knapsack([5], [10], 3) == 0
    assert len(lcs("ABCBDAB", "BDCABA")) == 4
    assert lcs("abc", "xyz") == ""
    assert lcs("", "abc") == ""
    assert lis_length([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert lis_length([]) == 0
    assert lis_length([5, 5, 5]) == 1
    assert matrix_chain([40, 20, 30, 10, 30]) == 26000
    assert matrix_chain([10, 20]) == 0
    print("All tests passed!")
