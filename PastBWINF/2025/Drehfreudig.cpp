#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O3")
namespace FastIO {
    inline void init() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
    }
}

unordered_map<int, int> adjSplitter(string& input) {
    unordered_map<int, vector<int>> adj;
    int parent = 0, curr = 1;
    for (int i = 0; i < input.size(); i++) {
        if (input[i] == ')' && curr != 1) {
            if (adj.find(curr) == adj.end()) adj[curr] = vector<int>();
            adj[parent].push_back(curr);
        }

    }

    return adj;
}

signed main() {
    FastIO::init();
    string input;
    cin >> input;
    
    return 0;
}