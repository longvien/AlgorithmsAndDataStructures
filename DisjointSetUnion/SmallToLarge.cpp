#include<bits/stdc++.h>
using namespace std;

signed main() {
    vector<vector<int>> v = {vector<int>(50), vector<int>(20), vector<int>(30)};
    vector<int> lg;
    lg = v[0];
    for (int i = 1; i < v.size(); i++) {
        for (int j = 0; j < v[i].size(); j++) {
            lg.push_back(v[i][j]);
        }
        v[i].clear();
    }
    cout << lg.size() << "\n"; 
    return 0;
} // Simulation ƒor Small To Large Technique. Optimized O(NlogN).