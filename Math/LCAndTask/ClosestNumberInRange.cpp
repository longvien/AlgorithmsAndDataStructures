#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O3")
#define f(i,a,n) for(int i = a; i<n; i++)
class Solution {
public:
    vector<bool> SieveOfErat(int n) {
        vector<bool> arr(n+1, true);
        arr[0] = false;
        arr[1] = false;
        f(i,2,(int)sqrt(n)+1) {
            if (arr[i]) {
                for (int j = i*i; j < n+1; j+=i) {
                    arr[j] = false;
                }
            }
        }
        return arr;
    }
    vector<int> closestPrimes(int left, int right) {
        vector<int> ans = {-1, -1};
        int diff = 1e6;
        int curr = 0;
        int prev = 0;
        vector<bool> rs = SieveOfErat(right);
        f(i,left,right+1) {
            if (rs[i]) {
                if (curr == 0) {curr = i;}
                else {
                    prev = curr;
                    curr = i;
                    if (curr-prev < diff) {
                        ans = {prev, curr};
                        diff = curr-prev;
                    }
                }
            }
        }
        return ans;
    }
};