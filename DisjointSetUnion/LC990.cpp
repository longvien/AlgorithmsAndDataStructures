#pragma GCC optimize("O3")
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<char> pr;
    set<pair<char, char>> v;
    unordered_map<char, vector<char>> m;
    bool ans = true;
    Solution() {
        for (int i = 0; i < 26; i++) {
            pr.push_back(static_cast<char>(i+97));
        }
    }
    char find(char x) {
        int dg = x - '0' + 48;
        if (pr[dg-97]==x) return x;
        return pr[dg-97] = find(pr[dg-97]);
    }
    void unite(char a, char b, bool f) {
        int pA = static_cast<int>(find(a)), pB = static_cast<int>(find(b));
        if (pA > pB) swap(pA, pB);
        if (!f) {
            if (pA==pB) {ans = false; return;} 
            else {
                v.insert({pA, pB});
                m[pA].push_back(pB);
                m[pB].push_back(pA);
            }
        } else {
                if (pA!=pB) {
                    if (v.count({pA, pB}) == 0 && v.count({pB, pA}) == 0) {
                        pr[pB - 97] = pA;
                        for (int i = 0 ; i < m[pB].size(); i++) {
                            m[pA].push_back(m[pB][i]);
                            v.insert({pA, m[pB][i]});
                        }
                    } else {
                        ans = false; return;
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