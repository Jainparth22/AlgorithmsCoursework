// Counting Sort (supports negatives). Time O(n + k), Space O(n + k), Stable.
#include <bits/stdc++.h>
#include <cassert>
using namespace std;

vector<int> countingSort(const vector<int>& a) {
    if (a.empty()) return {};
    int lo = *min_element(a.begin(), a.end()), hi = *max_element(a.begin(), a.end());
    vector<int> count(hi - lo + 1, 0), out(a.size());
    for (int x : a) count[x - lo]++;
    for (size_t i = 1; i < count.size(); i++) count[i] += count[i - 1];
    for (int i = (int)a.size() - 1; i >= 0; i--) out[--count[a[i] - lo]] = a[i];
    return out;
}

int main() {
    vector<vector<int>> tests = {{4, 2, 2, 8, 3, 3, 1}, {}, {1}, {-3, 5, -3, 0}, {7, 7, 7}};
    for (auto t : tests) {
        auto e = t; sort(e.begin(), e.end());
        assert(countingSort(t) == e);
    }
    cout << "All tests passed!\n";
}
