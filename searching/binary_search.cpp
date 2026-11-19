// Binary Search (sorted input). Time O(log n), Space O(1).
#include <bits/stdc++.h>
#include <cassert>
using namespace std;

int binarySearch(const vector<int>& a, int target) {
    int lo = 0, hi = (int)a.size() - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;  // avoids overflow
        if (a[mid] == target) return mid;
        if (a[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}

int main() {
    vector<int> a = {1, 3, 5, 7, 9, 11};
    assert(binarySearch(a, 7) == 3);
    assert(binarySearch(a, 1) == 0);
    assert(binarySearch(a, 11) == 5);
    assert(binarySearch(a, 4) == -1);
    assert(binarySearch({}, 4) == -1);
    cout << "All tests passed!\n";
}
