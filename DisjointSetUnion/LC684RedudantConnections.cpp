#pragma GCC optimize("03")
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> p;
    int find(int x) {
        if (p[x]==x) return x;
        return p[x] = find(p[x]);
    }
    bool join(int a, int b) {
        int pA = find(a);
        int pB = find(b);
        if (pA!=pB){
            p[pB] = pA;
            return true;
        }
        return false;
    }
    vector<int> findRedundantConnection(vector<vector<int>>& e) {
        p = vector<int>(e.size());
        vector<int> ans = {};
        for(int i=0; i<e.size(); i++) p[i] = i;
        for(int i=0; i<e.size(); i++) {
            if(!join(e[i][0]-1,e[i][1]-1)) {
               ans = {e[i][0], e[i][1]};
               break;
            }
        }
        return ans;
    }
};

