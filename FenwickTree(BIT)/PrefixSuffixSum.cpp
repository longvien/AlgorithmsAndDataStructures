#include <bits/stdc++.h>
using namespace std;

vector<int> PrefixSum(vector<int> nums) {
    vector<int> pref(nums.size());
    pref[0] = nums[0];
    for (size_t i = 1; i < nums.size(); i++) {
        pref[i] = pref[i-1] + nums[i];
    }
    return pref;
}

vector<int> SuffixSum(vector<int> nums) {
    int sz = nums.size();
    vector<int> suff(sz);
    suff[sz-1] = nums[sz-1];
    for (int i = sz-2; i >= 0; i--) {
        suff[i] = suff[i+1] + nums[i];
    }
    return suff;
}

int main() {
    vector<int> IN = {1,2,3};
    vector<int> suffix = SuffixSum(IN);
    vector<int> preffix = PrefixSum(IN);
    for (int i = 0; i < suffix.size(); i++) {
        cout << suffix[i] << " "; 
    }
    cout << "\n";
    for (int i = 0; i < suffix.size(); i++) {
        cout << preffix[i] << " "; 
    }
    cout << "\n";
    return 0;
}