#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O3, unroll-loops")

class Solution {
public:
    int maxCoins(vector<int>& nums) {
        if (nums.size() == 1) {return nums[0];}
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int i = 1; i < n-1; i++) {
            dp[i][i] = nums[i-1] * nums[i] * nums[i+1];
        }
        for (int i = n-2; i > 0; i--) {
            for (int j = i+1; j < n-1; j++) {
                for (int k = i; k < j+1; k++) {
                    int l = (k!=i)? dp[i][k-1] : 0;
                    int r = (k!=j)? dp[k+1][j] : 0;
                    dp[i][j] = max(dp[i][j], l + r + nums[i-1] * nums[k] * nums[j+1]);
                }
            }
        }
        return dp[1][n-2];
    }
};

/* dp idea: consider that k is the last ballon that is burst in the arr, what is the max points reachable? 
State: dp[i][j] = left + right + arr[i-1] * arr[k] * arr[j+1]. 
Base case: dp[i][i] = arr[i-1] * arr[i] * arr[i+1]

In which left is the max achieveable val to the left from k -> k-1 and 
right the max achv. val to the right from k -> k+1. |i---, k-1, k, k+1,---j| together we have dp[i][k-1] && dp[k+1][j] 
as ref. neighbour. i - 1 and j+1 stand for the outer neighbour of the sub-arr. Since all the ballon are bursted at the end, 
we have i-1 and j+1 left to multiply with k. => arr[i-1] * arr[k] * arr[j+1]. Together, we have the upper state for each targetted cell (i, j)*/