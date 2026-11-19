// Selection Sort. Time O(n^2) all cases, Space O(1), Not stable.
#include <bits/stdc++.h>
#include <cassert>
using namespace std;

void selectionSort(vector<int>& a) {
    int n = a.size();
    for (int i = 0; i + 1 < n; i++) {
        int m = i;
        for (int j = i + 1; j < n; j++) if (a[j] < a[m]) m = j;
        swap(a[i], a[m]);
    }
}

int main() {
    vector<vector<int>> tests = {{64, 25, 12, 22, 11}, {}, {1}, {3, 1, 3, 2}, {-2, -5, 0}};
    for (auto t : tests) {
        auto e = t; sort(e.begin(), e.end());
        selectionSort(t);
        assert(t == e);
    }
    cout << "All tests passed!\n";
}
