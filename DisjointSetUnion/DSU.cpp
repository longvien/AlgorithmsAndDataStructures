#include <bits/stdc++.h>
using namespace std;
//#pragma GCC optimize("O3")

struct ANS {
    vector<tuple<int, int, int>> ans;
    int cost;
};

class DSU {
    public:
    vector<int> pr, sz;
    
    DSU(int n) {
        pr = vector<int>(n);
        sz = vector<int>(n, 1);
        for (int i = 0; i < n; i++) pr[i] = i;
    }
    int find(int x) { // find + path compr
        if (pr[x]==x) return x;
        return pr[x] = find(pr[x]);
    }
    void unite(int a, int b) { // union by size
        int pA = find(a), pB = find(b);
        if (pA==pB) return;
        if (sz[pA] > sz[pB]) {
            pr[pB] = pA;
            sz[pB] += sz[pA];
        } else {
            pr[pA] = pB;
            sz[pA] += sz[pB];
        }
    }
    
    vector<tuple<int, int, int>> Kruskal(vector<tuple<int, int, int>>) {

    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ANS Kruskal(vector<tuple<int, int, int>> edges) {
        for (auto [a,b,c] : edges) {
            parent[a] = a; size[a] = 1;
            parent[b] = b; size[b] = 1;
        }
        sort(edges.begin(), edges.end(), [](const auto& a, const auto& b) {return get<2>(a) < get<2>(b);});
        int cost = 0;
        vector<tuple<int, int, int>> ans;
        for (auto [a, b, c] : edges) {
            int pA = find(a), pB = find(b);
            if (pA==pB) continue;
            join (pA, pB);
            ans.emplace_back(a,b,c);
            cost += c
        }
        ANS n;
        n.cost = cost;
        n.ans = ans;
        return n;
    }
};

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    DSU obj(4);
    ANS out = obj.Kruskal({{1,2,4}, {1,3,1}, {3,4,2}, {2,4,3}});
    cout << out.cost << "\n";
    for (auto [a,b,c] : out.ans) {
        cout << a << " " << b << " " << c << "\n";
    }
    return 0;    
}