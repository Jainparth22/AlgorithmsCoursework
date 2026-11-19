// LSD Radix Sort (base 10, supports negatives). Time O(d*(n+b)), Space O(n+b), Stable.
#include <bits/stdc++.h>
#include <cassert>
using namespace std;

vector<int> byDigit(const vector<int>& a, long long exp) {
    vector<int> out(a.size()), count(10, 0);
    for (int x : a) count[(x / exp) % 10]++;
    for (int i = 1; i < 10; i++) count[i] += count[i - 1];
    for (int i = (int)a.size() - 1; i >= 0; i--) out[--count[(a[i] / exp) % 10]] = a[i];
    return out;
}

vector<int> radixNonNeg(vector<int> a) {
    if (a.empty()) return a;
    int mx = *max_element(a.begin(), a.end());
    for (long long exp = 1; mx / exp > 0; exp *= 10) a = byDigit(a, exp);
    return a;
}

vector<int> radixSort(const vector<int>& a) {
    vector<int> neg, pos;
    for (int x : a) (x < 0 ? neg : pos).push_back(abs(x));
    neg = radixNonNeg(neg); pos = radixNonNeg(pos);
    vector<int> out;
    for (int i = (int)neg.size() - 1; i >= 0; i--) out.push_back(-neg[i]);
    out.insert(out.end(), pos.begin(), pos.end());
    return out;
}

int main() {
    vector<vector<int>> tests = {{170, 45, 75, 90, 802, 24, 2, 66}, {}, {5}, {-3, 12, -100, 0, 7}, {9, 9, 1}};
    for (auto t : tests) {
        auto e = t; sort(e.begin(), e.end());
        assert(radixSort(t) == e);
    }
    cout << "All tests passed!\n";
}
