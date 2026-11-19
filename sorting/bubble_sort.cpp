/*
 * Bubble Sort
 * Time:  O(n²) average/worst, O(n) best (already sorted)
 * Space: O(1) in-place
 * Stable: YES
 *
 * Optimization: early exit if no swaps in a full pass (already sorted).
 */

#include <bits/stdc++.h>
#include <cassert>
using namespace std;

void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        // After pass i, the i largest elements are at the end
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;  // already sorted — early exit
    }
}

void printArr(const vector<int>& arr) {
    for (int x : arr) cout << x << " ";
    cout << "\n";
}

int main() {
    // Test 1: general case
    vector<int> a = {64, 34, 25, 12, 22, 11, 90};
    bubbleSort(a);
    cout << "Test 1: "; printArr(a);  // 11 12 22 25 34 64 90

    // Test 2: already sorted (early exit kicks in)
    vector<int> b = {1, 2, 3, 4, 5};
    bubbleSort(b);
    cout << "Test 2: "; printArr(b);  // 1 2 3 4 5

    // Test 3: reverse sorted (worst case)
    vector<int> c = {5, 4, 3, 2, 1};
    bubbleSort(c);
    cout << "Test 3: "; printArr(c);  // 1 2 3 4 5

    // Test 4: single element
    vector<int> d = {42};
    bubbleSort(d);
    cout << "Test 4: "; printArr(d);  // 42

    // Test 5: duplicates
    vector<int> e = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3};
    bubbleSort(e);
    cout << "Test 5: "; printArr(e);  // 1 1 2 3 3 4 5 5 6 9

    return 0;
}
