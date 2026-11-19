// Linear Search. Time O(n), Space O(1). Works on unsorted data.
#include <bits/stdc++.h>
#include <cassert>
using namespace std;

int linearSearch(const vector<int>& a, int target) {
    for (int i = 0; i < (int)a.size(); i++) if (a[i] == target) return i;
    return -1;
}

int main() {
    assert(linearSearch({4, 2, 7, 2}, 2) == 1);
    assert(linearSearch({4, 2, 7}, 9) == -1);
    assert(linearSearch({}, 1) == -1);
    cout << "All tests passed!\n";
}
