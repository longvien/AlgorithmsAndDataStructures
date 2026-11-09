#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<char> pr;
    vector<int> sz;
    set<pair<char, char>> v;
    bool ans = true;
    for (int i = 0; i < 26; i++) {
        pr.push_back(static_cast<char>(i+97));
        sz.push_back(1);
    }
    char find(char x) {
        int dg = x - '0';
        if (pr[dg-97]==) return x;
        return pr[x] = find(pr[x]);
    }
    void unite(int a, int b, bool f) {
        int pA = find(a), pB = find(b);
        if (!f) {
            if (pA==pB) { ans = false; return; } 
            else { v.insert({pA, pB}); }
        } else {
                if (pA!=pB) {
                    if (v.count({pA, pB}) == 0) {
                        if (sz[pA] > sz[pB]) { pr[pB] = pA; sz[pA] += sz[pB]; }
                        else  { pr[pA] = pB; sz[pB] += sz[pA];}
                    }
                }
        }
        
    }
    bool equationsPossible(vector<string>& e) {
        for (int i = 0; i < e.size(); i++) {
            if (e[i][1] == '!') {
                unite(e[i][0], e[i][3], false);
            } else {
                unite(e[i][0], e[i][3], true);
            }
            if (!ans) return ans;
        }
        return ans;
    }
};
signed main() {
    Solution n = Solution();
    vector<string> s = {"a==b","b!=a"};
    cout << n.equationsPossible(s) << "\n";
}


