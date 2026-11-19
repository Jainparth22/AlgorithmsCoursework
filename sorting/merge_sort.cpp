/*
 * Merge Sort
 * Time:  O(n log n) — always (best, average, worst)
 * Space: O(n) auxiliary
 * Stable: YES
 *
 * Divide and conquer:
 *   1. Split array in half recursively until size 1
 *   2. Merge two sorted halves back together
 *
 * Use when: stable sort needed, sorting linked lists, external sort.
 */

#include <bits/stdc++.h>
#include <cassert>
using namespace std;

void merge(vector<int>& arr, int l, int m, int r) {
    // Merge arr[l..m] and arr[m+1..r] (both sorted)
    vector<int> left(arr.begin() + l, arr.begin() + m + 1);
    vector<int> right(arr.begin() + m + 1, arr.begin() + r + 1);

    int i = 0, j = 0, k = l;
    while (i < (int)left.size() && j < (int)right.size()) {
        // <= for stability (preserve relative order of equal elements)
        arr[k++] = (left[i] <= right[j]) ? left[i++] : right[j++];
    }
    while (i < (int)left.size())  arr[k++] = left[i++];
    while (j < (int)right.size()) arr[k++] = right[j++];
}

void mergeSort(vector<int>& arr, int l, int r) {
    if (l >= r) return;           // base case: one element
    int m = l + (r - l) / 2;     // avoid integer overflow vs (l+r)/2
    mergeSort(arr, l, m);         // sort left half
    mergeSort(arr, m + 1, r);     // sort right half
    merge(arr, l, m, r);          // merge sorted halves
}

void printArr(const vector<int>& arr) {
    for (int x : arr) cout << x << " ";
    cout << "\n";
}

int main() {
    // Test 1: general
    vector<int> a = {38, 27, 43, 3, 9, 82, 10};
    mergeSort(a, 0, a.size() - 1);
    cout << "Test 1: "; printArr(a);  // 3 9 10 27 38 43 82

    // Test 2: already sorted
    vector<int> b = {1, 2, 3, 4, 5};
    mergeSort(b, 0, b.size() - 1);
    cout << "Test 2: "; printArr(b);  // 1 2 3 4 5

    // Test 3: reverse sorted
    vector<int> c = {5, 4, 3, 2, 1};
    mergeSort(c, 0, c.size() - 1);
    cout << "Test 3: "; printArr(c);  // 1 2 3 4 5

    // Test 4: single element
    vector<int> d = {7};
    mergeSort(d, 0, d.size() - 1);
    cout << "Test 4: "; printArr(d);  // 7

    // Test 5: duplicates
    vector<int> e = {5, 2, 8, 2, 5, 1};
    mergeSort(e, 0, e.size() - 1);
    cout << "Test 5: "; printArr(e);  // 1 2 2 5 5 8

    return 0;
}
