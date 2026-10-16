#include <bits/stdc++.h>
using namespace std;
//#pragma GCC optimize("O3")

struct ANS {
    vector<tuple<int, int, int>> ans;
    int cost;
};

class DSU {
    public:
    vector<int> parent, size;
    
    DSU(int x) {
        for (int i = 0; i < x; i++) {
            parent.push_back(i);
            size.push_back(1);
        }
    }
    
    int find(int x) {
        if (parent[x] == x) return parent[x];
        return parent[x] = find(parent[x]);
    }

    void join(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);
        if (size[rootA] < size[rootB]) {
            parent[rootA] = rootB; 
            size[rootB]+=size[rootA]; 
        }
        else { 
            parent[rootB] = rootA; size[rootA] += size[rootB]; 
        }
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
            cost += c;
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