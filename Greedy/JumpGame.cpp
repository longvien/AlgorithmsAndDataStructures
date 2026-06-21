class Solution {
public:
    bool canJump(vector<int>& nums) {
        if (nums.size() == 1) { return true; }
        if (nums[0] == 0) { return false; }
        int curr = 0;
        int reachAble = nums[0];
        bool valid = true;
        bool done = false;
        while (valid && !done) {
            if (reachAble == 0) {
                valid = false;
                break;
            }
            int cIn = 0;
            int cR = 0;
            int fI = curr;
            for (int i = 1; i < reachAble + 1; i++) {
                cIn = curr + i;
                if (cIn + nums[cIn] >= nums.size() - 1) {
                    done = true;
                    break;
                }
                else if (cIn + nums[cIn] >= cR) {
                    cR = cIn + nums[cIn];
                    fI = cIn;
                }
            }
            curr = fI;
            reachAble = nums[curr];
        }
        return valid;
    }
};