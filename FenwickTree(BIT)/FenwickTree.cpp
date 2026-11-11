#include <bits/stdc++.h>
using namespace std;
using ll = long long;
// The Standard Fenwick Tree
struct StandardBIT {
    int n;
    vector<int> bit;
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
        if (r+1 <= n) {
            update(r+1, -delta);
        }
    }
};

// Fenwick Tree with Range Update & Range Query | 2 BITs
struct RangeQueryBIT {
    int n;
    vector<int> bit1;
    vector<int> bit2;
    RangeQueryBIT(int n) {
        this->n = n;
        bit1 = vector<int>(n+1, 0);
        bit2 = vector<int>(n+1, 0);
    }
    void updateB1(int i, int delta) {
        for (; i <= n; i += i&-i) {
            bit1[i] += delta; 
        }
    }
    void updateB2(int i , int delta) {
        for (; i <= n; i += i & -i) {
            bit2[i] += i*delta;
        }
    }
    void updateRange(int l, int r, int delta) {
        updateB1(l, delta);
        updateB2(l, delta);
        if (r+1 <= n) {
            updateB1(r+1, -delta);
            updateB2(r+1, -delta);
        }
    }
    int queryB1(int i) {
        int total = 0;
        for (; i > 0; i-=i&-i) {
            total += bit1[i];
        }
        return total;
    }
    int queryB2(int i) {
        int total = 0;
        for (; i > 0 ; i-=i & -i) {
            total += bit2[i];
        }
        return total;
    }
    int rangeSumQuery(int l, int r) {
        return ((r+1)*queryB1(r) - queryB2(r)) - (l*queryB1(l-1) - queryB2(l-1)); 
    }
 };


signed main() {
    StandardBIT b0(4);
    b0.update(1, 2);
    b0.update(2, 3);
    b0.update(3, 5);
    b0.update(4, 4);
    cout << "Preffix Sum Query on Standard BIT" << "\n";
    for (int i = 1; i <= 4; i++) {
        cout << b0.preffixSumQuery(i) << " ";
    }
    cout << "\n" << "Range Sum Query on Standard BIT: " << b0.rangeSum(1,4) << "\n";
    DifferenceBIT b1(4);
    b1.update(1, 2);
    b1.update(2, 1);
    b1.update(3, 2);
    b1.update(4, -1);
    b1.rangeUpdate(1, 3, 10);
    cout << "Point Query on Difference BIT after range update: " << b1.pointQuery(3) << "\n";
    
    RangeQueryBIT b2(4);
    vector<int> diff = {2, 1, 2, -1};
    for (int i = 1; i <= 4; i++) {
        b2.updateB1(i, diff[i-1]);
        b2.updateB2(i, diff[i-1]);
    }
    b2.updateRange(1, 3, 20);
    cout << b2.rangeSumQuery(1, 3) << "\n";
    return 0;
}