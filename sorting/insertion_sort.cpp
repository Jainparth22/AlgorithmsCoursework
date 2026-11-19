// Insertion Sort. Time O(n) best / O(n^2) avg+worst, Space O(1), Stable.
#include <bits/stdc++.h>
#include <cassert>
using namespace std;

void insertionSort(vector<int>& a) {
    for (int i = 1; i < (int)a.size(); i++) {
        int key = a[i], j = i - 1;
        while (j >= 0 && a[j] > key) { a[j + 1] = a[j]; j--; }
        a[j + 1] = key;
    }
}

int main() {
    vector<vector<int>> tests = {{12, 11, 13, 5, 6}, {}, {1}, {3, 1, 3, 2}, {-2, -5, 0}, {1, 2, 3}};
    for (auto t : tests) {
        auto e = t; sort(e.begin(), e.end());
        insertionSort(t);
        assert(t == e);
    }
    cout << "All tests passed!\n";
}
