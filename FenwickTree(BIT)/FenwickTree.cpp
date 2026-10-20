#include <bits/stdc++.h>
using namespace std;

class FenwickTree {
    public:
    vector<int> IN;
    vector<int> Fenwick;
    FenwickTree(int n, vector<int> IN) {
        Fenwick = vector<int>(n+1);
        this.IN = IN;
    }
    int lowbit(int x) {
        return x & -x;
    }
    int rangeSumQuery(int l, int r) [

    ]
    void update(int i, int delta) {
        for (int j = i; j < )
    }
}

signed main() {
    return 0;
}