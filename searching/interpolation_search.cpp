// Interpolation Search (sorted, uniform data). Time O(log log n) avg, O(n) worst, Space O(1).
#include <bits/stdc++.h>
#include <cassert>
using namespace std;

int interpolationSearch(const vector<int>& a, int target) {
    int lo = 0, hi = (int)a.size() - 1;
    while (lo <= hi && target >= a[lo] && target <= a[hi]) {
        if (a[hi] == a[lo]) return a[lo] == target ? lo : -1;
        long long pos = lo + (long long)(target - a[lo]) * (hi - lo) / ((long long)a[hi] - a[lo]);
        if (a[pos] == target) return (int)pos;
        if (a[pos] < target) lo = (int)pos + 1;
        else hi = (int)pos - 1;
    }
    return -1;
}

int main() {
    vector<int> a = {10, 20, 30, 40, 50, 60, 70};
    assert(interpolationSearch(a, 50) == 4);
    assert(interpolationSearch(a, 10) == 0);
    assert(interpolationSearch(a, 70) == 6);
    assert(interpolationSearch(a, 35) == -1);
    assert(interpolationSearch({}, 1) == -1);
    cout << "All tests passed!\n";
}
