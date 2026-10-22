#include <bits/stdc++.h>
using namespace std;

class NumArray {
public:
    vector<int> n, fw;
    NumArray(vector<int>& nums) {
        this->n = nums;
        fw = vector<int>(nums.size()+1, 0);
        for(int i=0; i<nums.size(); i++) {
            for (int j=i+1; j<fw.size(); j+=(j&-j)) {
                fw[j] += nums[i];
            }
        }
    }
    void update(int i, int val) {
        int diff = val-n[i];
        n[i] = val;
        i+=1;
        for(; i<fw.size(); i+=(i&-i)) {
            fw[i] += diff;
        }
    }
    int query(int i) {
        i+=1;
        int total = 0;
        for (; i>0; i-=(i&-i)) {
            total += fw[i];
        }
        return total;
    }
    
    int sumRange(int left, int right) {
       if (left==0) return query(right);
       else return query(right) - query(left-1);
    }
};