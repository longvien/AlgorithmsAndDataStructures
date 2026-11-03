#include<bits/stdc++.h>
using namespace std;

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> small = {0, 1, 2,4,5,6,6,7};
    vector<int> large = {4, 5, 6, 7}; 
    if (small.size() > large.size()) swap(small, large);
    int sS = small.size(), lS = large.size();
    for (int i = sS - 1; i >= 0; i--) {
        large.push_back(small[i]);
        small.pop_back();
    }
    cout << large.size() << "\n";
    return 0;
} // Simulation ƒor Small To Large Technique in CP