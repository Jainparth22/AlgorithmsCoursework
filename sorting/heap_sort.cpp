// Heap Sort. Time O(n log n) all cases, Space O(1), Not stable.
#include <bits/stdc++.h>
#include <cassert>
using namespace std;

void siftDown(vector<int>& a, int i, int n) {
    while (true) {
        int largest = i, l = 2 * i + 1, r = 2 * i + 2;
        if (l < n && a[l] > a[largest]) largest = l;
        if (r < n && a[r] > a[largest]) largest = r;
        if (largest == i) return;
        swap(a[i], a[largest]);
        i = largest;
    }
}

void heapSort(vector<int>& a) {
    int n = a.size();
    for (int i = n / 2 - 1; i >= 0; i--) siftDown(a, i, n);
    for (int end = n - 1; end > 0; end--) { swap(a[0], a[end]); siftDown(a, 0, end); }
}

int main() {
    vector<vector<int>> tests = {{12, 11, 13, 5, 6, 7}, {}, {1}, {3, 1, 3, 2}, {-2, -5, 0}};
    for (auto t : tests) {
        auto e = t; sort(e.begin(), e.end());
        heapSort(t);
        assert(t == e);
    }
    cout << "All tests passed!\n";
}
