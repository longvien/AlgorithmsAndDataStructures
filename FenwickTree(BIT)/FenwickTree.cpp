#include <bits/stdc++.h>
using namespace std;

class FenwickTree {
    public:
    deque<int> IN;
    vector<int> Fenwick, diff;
    FenwickTree(deque<int> IN) { // Build
        Fenwick = vector<int>(IN.size()+1, 0);
        diff = vector<int>(IN.size()+1, 0);
        this->IN = IN;
        this->IN.push_front(0);
        for (int i = 1; i < this->IN.size(); i++) {
            int currDiff = (this->IN[i] - this->IN[i-1]);
            for (int j = i; j < this->Fenwick.size(); j += (j&-j)) {
                this->Fenwick[j] += this->IN[i];
                this->diff[j] += currDiff;
            }   
        }
    }
    //int lowbit(int x) { return x & -x; } lowbit Calc.
    int preffixQueryF (int i) { // PreffixQuery
        if (i==0) return 0;
        int total = 0;
        for (; i>0; i -= (i & -i)) total += Fenwick[i];
        return total;
    }
    int rangeSumQuery(int l, int r) {return preffixQueryF(r) - preffixQueryF(l-1);} // rangeSumQuery
    void rangeUpdate(int l, int r, int delta) {
        diff[l] += delta;
        diff[r+1] -= delta;
    }
    void update(int i, int delta) {
        for (int j = i; j < Fenwick.size(); j += (j&-j)) {
            Fenwick[j] += delta;
        }
    } // PointUpdate
    int get(int i) {
        if (i==0) return 0;
        int total = 0;
        for (; i>0; i-= (i & -i)) total += diff[i];
        return total;
    }
};

signed main() {
    deque<int> IN = {2, 4, 1, 3, 5};
    FenwickTree f1(IN);
    f1.update(2, 5);
    f1.rangeUpdate(2,4,5);
    cout << f1.rangeSumQuery(1, 2) << "\n";
    cout << f1.get(2) << "\n";
    return 0;
}