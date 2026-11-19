"""Shortest-path algorithms: Dijkstra, Bellman-Ford, Floyd-Warshall."""
import heapq
from typing import Dict, List, Tuple

INF = float("inf")


def dijkstra(g: Dict[int, List[Tuple[int, int]]], src: int, n: int) -> List[float]:
    """Non-negative weights. g[u] = [(v, w), ...]. Time O((V+E) log V)."""
    dist = [INF] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in g.get(u, []):
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist


def bellman_ford(n: int, edges: List[Tuple[int, int, int]], src: int):
    """Handles negative weights. Returns dist list, or None on a negative cycle.
    Time O(V*E)."""
    dist = [INF] * n
    dist[src] = 0
    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return None
    return dist


def floyd_warshall(n: int, edges: List[Tuple[int, int, int]]) -> List[List[float]]:
    """All-pairs shortest paths. Time O(V^3)."""
    d = [[INF] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for u, v, w in edges:
        d[u][v] = min(d[u][v], w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    return d


if __name__ == "__main__":
    edges = [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5)]
    g = {}
    for u, v, w in edges:
        g.setdefault(u, []).append((v, w))
    assert dijkstra(g, 0, 5) == [0, 3, 1, 4, INF]
    assert bellman_ford(5, edges, 0) == [0, 3, 1, 4, INF]
    assert bellman_ford(3, [(0, 1, 1), (1, 2, -1), (2, 1, -1)], 0) is None
    assert bellman_ford(3, [(0, 1, 4), (1, 2, -2)], 0) == [0, 4, 2]
    fw = floyd_warshall(4, edges)
    assert fw[0] == [0, 3, 1, 4]
    assert fw[3][0] == INF
    print("All tests passed!")
