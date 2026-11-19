"""BFS and DFS on an adjacency-list graph. Time O(V + E), Space O(V)."""
from collections import deque
from typing import Dict, List

Graph = Dict[int, List[int]]


def bfs(g: Graph, start: int) -> List[int]:
    seen, order, q = {start}, [], deque([start])
    while q:
        u = q.popleft()
        order.append(u)
        for v in g.get(u, []):
            if v not in seen:
                seen.add(v)
                q.append(v)
    return order


def dfs(g: Graph, start: int) -> List[int]:
    seen, order = set(), []
    stack = [start]  # iterative: avoids recursion limit on deep graphs
    while stack:
        u = stack.pop()
        if u in seen:
            continue
        seen.add(u)
        order.append(u)
        for v in reversed(g.get(u, [])):
            if v not in seen:
                stack.append(v)
    return order


if __name__ == "__main__":
    g = {0: [1, 2], 1: [3], 2: [3, 4], 3: [5], 4: [5], 5: []}
    assert bfs(g, 0) == [0, 1, 2, 3, 4, 5]
    assert dfs(g, 0) == [0, 1, 3, 5, 2, 4]
    assert bfs({0: []}, 0) == [0]
    print("All tests passed!")
