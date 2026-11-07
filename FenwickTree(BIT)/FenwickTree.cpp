#include<bits/stdc++.h>
using namespace std;

class BIT {
    public:
    vector<int> arr, bit, diff;
    BIT(vector<int> n) {
        int p = (int)n.size();
        arr = n;
        diff = vector<int>(p); bit = vector<int>(p);
        diff[0] = bit[0];
        for (int i = 0; i < p; i++) {
            for(int j = i+1; j <= p; j += j&-j) {
                bit[j-1] += arr[i];
            }
        }
        for (int i = 1; i < p; i++) {
            diff[i] = arr[i]-arr[i-1];
        }
    }
    int p = (int)arr.size();
    int prefSum(int i) {
        i++;
        int count = 0;
        for (; i >= 1; i -= i&-i) {
            count += bit[i-1];
        }
        return count;
    }
    
    int rangeSum(int l, int r) {
        r++; l++;
        return prefSum(r) - prefSum(l-1);
    }
    
    void pointUpdate(int i, int u) {
        i++;
        for (; i <= p; i += i&-i) {
            bit[i-1] += u;
        }
    }
    
    void rangeUpdate(int l , int r, int u) {
        l++; r++;
        diff[l-1] += u;
        diff[r] -= u;
    }

    int pointQueryARangeUpdate(int i) {
        int count = 0;
        for(; i >= 0; i-- ) {
            count += diff[i];
        }
        return count;
    }
    
    int prefSumARangeUpdate(int i) {
        for (int j = i; j>=0; j--) {

        }
    }
    
    int rangeSumARangeUpdate(int l, int r) {
        for (i >= )
        return 0;
    }
 
}


