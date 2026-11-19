"""String matching: KMP, Rabin-Karp, Z-algorithm. Each returns all match start indices."""
from typing import List


def kmp(text: str, pat: str) -> List[int]:
    """Time O(n + m)."""
    if not pat:
        return []
    fail = [0] * len(pat)
    k = 0
    for i in range(1, len(pat)):
        while k and pat[i] != pat[k]:
            k = fail[k - 1]
        if pat[i] == pat[k]:
            k += 1
        fail[i] = k
    res, k = [], 0
    for i, c in enumerate(text):
        while k and c != pat[k]:
            k = fail[k - 1]
        if c == pat[k]:
            k += 1
        if k == len(pat):
            res.append(i - k + 1)
            k = fail[k - 1]
    return res


def rabin_karp(text: str, pat: str, base: int = 256, mod: int = 1_000_000_007) -> List[int]:
    """Rolling hash; verifies candidates. Time O(n + m) avg."""
    n, m = len(text), len(pat)
    if m == 0 or m > n:
        return []
    high = pow(base, m - 1, mod)
    hp = ht = 0
    for i in range(m):
        hp = (hp * base + ord(pat[i])) % mod
        ht = (ht * base + ord(text[i])) % mod
    res = []
    for i in range(n - m + 1):
        if hp == ht and text[i:i + m] == pat:
            res.append(i)
        if i < n - m:
            ht = ((ht - ord(text[i]) * high) * base + ord(text[i + m])) % mod
    return res


def z_array(s: str) -> List[int]:
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


def z_search(text: str, pat: str) -> List[int]:
    """Time O(n + m). Uses a separator that cannot occur in the input."""
    if not pat:
        return []
    sep = "\x00"
    z = z_array(pat + sep + text)
    m = len(pat)
    return [i - m - 1 for i in range(m + 1, len(z)) if z[i] == m]


if __name__ == "__main__":
    for f in (kmp, rabin_karp, z_search):
        assert f("abxabcabcaby", "abcaby") == [6], f.__name__
        assert f("aaaaa", "aa") == [0, 1, 2, 3], f.__name__  # overlapping
        assert f("hello", "xyz") == [], f.__name__
        assert f("abc", "") == [], f.__name__
        assert f("ab", "abc") == [], f.__name__
    assert z_array("aabxaab") == [0, 1, 0, 0, 3, 1, 0]
    print("All tests passed!")
