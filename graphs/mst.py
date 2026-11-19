"""Minimum spanning tree: Kruskal (union-find) and Prim (heap). O(E log V)."""
import heapq
from typing import List, Tuple

Edge = Tuple[int, int, int]  # (u, v, w)


def kruskal(n: int, edges: List[Edge]) -> Tuple[int, List[Edge]]:
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # path halving
            x = parent[x]
        return x

    total, used = 0, []
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
            total += w
            used.append((u, v, w))
    return total, used


def prim(n: int, edges: List[Edge]) -> int:
    """Total MST weight of the component containing vertex 0."""
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((w, v))
        adj[v].append((w, u))
    seen, total = [False] * n, 0
    pq = [(0, 0)]
    while pq:
        w, u = heapq.heappop(pq)
        if seen[u]:
            continue
        seen[u] = True
        total += w
        for w2, v in adj[u]:
            if not seen[v]:
                heapq.heappush(pq, (w2, v))
    return total


if __name__ == "__main__":
    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    total, used = kruskal(4, edges)
    assert total == 19 and len(used) == 3
    assert prim(4, edges) == 19
    assert kruskal(1, [])[0] == 0
    print("All tests passed!")
