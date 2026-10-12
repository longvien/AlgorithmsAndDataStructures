#include <bits/stdc++.h>
using namespace std;
//#pragma GCC optimize("O3")

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
};

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    DSU obj(4);
    obj.join(1,2);
    cout << obj.find(2) << "\n";
    return 0;    
}