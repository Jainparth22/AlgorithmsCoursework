# Algorithms Coursework

> Classic algorithm implementations in C++ and Python, organized by topic. Built as a companion to coursework at VIT Bhopal.

[![C++](https://img.shields.io/badge/C++-17-00599C)](https://en.cppreference.com)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)

---

## Contents

| Category | Algorithms | Languages | Status |
|----------|-----------|-----------|--------|
| Sorting | Bubble, Selection, Insertion, Merge, Quick, Heap, Counting, Radix | C++ & Python | ✅ Done |
| Searching | Linear, Binary, Interpolation | C++ & Python | ✅ Done |
| Graph | BFS, DFS, Dijkstra, Bellman-Ford, Floyd-Warshall, Kruskal, Prim | Python | ✅ Done |
| Dynamic Programming | 0/1 Knapsack, LCS, LIS, Matrix Chain | Python | ✅ Done |
| String | KMP, Rabin-Karp, Z-algorithm | Python | ✅ Done |
| Trees | BST, AVL rotations, Segment Tree | Python | ✅ Done |
| Backtracking | N-Queens, Sudoku, Subset Sum | Python | ✅ Done |

Every file has built-in tests: Python files use `assert` and print `All tests passed!`.

---

## Structure

```
AlgorithmsCoursework/
├── sorting/         # 8 algorithms, each as .cpp + .py
├── searching/       # linear, binary, interpolation (.cpp + .py)
├── graphs/          # traversal.py, shortest_paths.py, mst.py
├── dp/              # classic_dp.py
├── strings/         # string_matching.py
├── trees/           # bst.py, avl.py, segment_tree.py
├── backtracking/    # backtracking.py
└── README.md
```

---

## How to Compile & Run

### C++
```bash
g++ -std=c++17 -O2 -o out sorting/bubble_sort.cpp
./out
```

### Python
```bash
python sorting/bubble_sort.py
python graphs/shortest_paths.py
```

---

## Complexity Reference

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ❌ |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(n+k) | ✅ |
| Radix Sort | O(d(n+b)) | O(d(n+b)) | O(d(n+b)) | O(n+b) | ✅ |
| Linear Search | O(1) | O(n) | O(n) | O(1) | — |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) | — |
| Interpolation Search | O(1) | O(log log n) | O(n) | O(1) | — |
| Dijkstra | — | O((V+E) log V) | O((V+E) log V) | O(V) | — |

---

## Resources

- [CLRS — Introduction to Algorithms](https://mitpress.mit.edu/9780262046305/)
- [CP-Algorithms](https://cp-algorithms.com)
- [Visualgo](https://visualgo.net)
