// #pragma GCC optimize("03")
#include <bits/stdc++.h>
using namespace std;

namespace FastIO {
    inline void init() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
    }
};
// Invariant: w[a] = v[a] - v[parent[a]]
class DifferenceDSU {
    public:
        vector<int> parent;
        vector<int> weight;
        DifferenceDSU(int x)
            : parent(x),
            weight(x, 0)
        {
            iota(parent.begin(), parent.end(), 0);
        }
        int find(int x) {
            if (parent[x] == x) return x;
            int oldPr = parent[x];
            parent[x] = find(parent[x]); 
            weight[x] += weight[oldPr];
            return parent[x];       
        }

        void unite(int a, int b, int d) {
            int parentA = find(a);
            int parentB = find(b);
            if (parentA != parentB) {
                parent[parentA] = parentB;
                weight[parentA] = d - weight[a] + weight[b];
            }
        }
};

signed main() {
    FastIO::init();
    DifferenceDSU obj(6);
    obj.unite(1,2,4);
    obj.unite(3,4,5);
    cout << obj.find(1) << "\n";
    obj.unite(1,3,2);
    cout << obj.find(1) << "\n";
    cout << obj.weight[1] << "\n";
    return 0;
}