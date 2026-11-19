// Quick Sort (Lomuto, random pivot). Time O(n log n) avg / O(n^2) worst, Space O(log n), Not stable.
#include <bits/stdc++.h>
#include <cassert>
using namespace std;

mt19937 rng(12345);

int partitionRange(vector<int>& a, int lo, int hi) {
    int r = lo + rng() % (hi - lo + 1);
    swap(a[r], a[hi]);
    int pivot = a[hi], i = lo;
    for (int j = lo; j < hi; j++)
        if (a[j] < pivot) swap(a[i++], a[j]);
    swap(a[i], a[hi]);
    return i;
}

void quickSort(vector<int>& a, int lo, int hi) {
    while (lo < hi) {
        int p = partitionRange(a, lo, hi);
        if (p - lo < hi - p) { quickSort(a, lo, p - 1); lo = p + 1; }
        else { quickSort(a, p + 1, hi); hi = p - 1; }
    }
}

int main() {
    vector<vector<int>> tests = {{10, 7, 8, 9, 1, 5}, {}, {1}, {3, 1, 3, 2}, {-2, -5, 0}, vector<int>(10, 5)};
    for (auto t : tests) {
        auto e = t; sort(e.begin(), e.end());
        quickSort(t, 0, (int)t.size() - 1);
        assert(t == e);
    }
    cout << "All tests passed!\n";
}
