#include <bits/stdc++.h>

class Solution {
public:
    bool validPartition(vector<int>& nums) {
        vector<int> dp(nums.size() + 1, false);
            dp[0] = true;
            dp[1] = false;
            for (int i = 1; i < nums.size(); i++) {
                if (nums[i] == nums[i-1]) {
                    if (dp[i-1]) {
                        dp[i+1] = true;
                    }
                    else {
                        if (nums[i] == nums[i-2] && dp[i]) {
                            dp[i+1] = true;
                        }
                    }
                }
                else if (i >= 2) {
                    if (nums[i] - nums[i - 1] == 1) {
                        if (nums[i - 1] - nums[i - 2] == 1) {
                            if (dp[i - 2]) {
                                dp[i+1] = true;
                            }
                        }
                    }
                }
            } 
        return dp[nums.size()];
    }
};