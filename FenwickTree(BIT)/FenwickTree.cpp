#include <bits/stdc++.h>
using namespace std;

// The Standard Fenwick Tree
struct StandardBIT {
    int n;
    vecotor<int> bit;
    StandardBIT(int n) {
        this->n = n;
        bit = vector<int>(n+1, 0);
    }
    void update(int i , int delta) {
        for (; i <= n; i += i & -i) {
            bit[i] += delta;
        }
    }
    int preffixSumQuery(int i) {
        int total = 0;
        for (; i > 0; i -= i & -i) {
            total += bit[i];
        }
        return total;
    }
    int rangeSum(int l, int r) {
        return preffixSumQuery(r) - preffixSumQuery(l-1);
    }
};

// Fenwick Tree with Range Update + Point Query possible. | One of the most useful BIT variation in CP!!!
struct DifferenceBIT {
    int n;
    vector<int> diff;
    DifferenceBIT(int n) {
        this->n = n;
        diff = vector<int>(n+1, 0);
    }
    void update(int i, int delta) {
        for (; i <= n; i += i & -i) {
            diff[i] += delta;        
        }
    }
    int pointQuery(int i) {
        int total = 0;
        for (; i > 0; i -= i&-i) {
            total += diff[i];
        }
        return total;
    }
    void rangeUpdate(int l , int r, int delta) {
        update(l, delta);
        if (r+1 < n) {
            update(r+1, -delta);
        }
    }
};

// Fenwick Tree with Range Update & Range Query | 2 BITs
struct RangeQueryBIT {
    int n;
    vector<int> diff;
    vector<int> bit;
    RangeQueryBIT(int n) {
        this->n = n;
        diff = vector<int>(n+1, 0);
        bit = vector<int>(n+1, 0);
    }
    void update(int i, int delta) {
        for (; i <= n; i += i&-i) {
            
        }
    }


 };


signed main() {
    
    return 0;
}