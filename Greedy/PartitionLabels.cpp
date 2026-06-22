#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> partitionLabels(string s) {
        vector<int> ans;
        vector<vector<int>> intervals;
        unordered_map<char, vector<int>> indexes;
        for (int i = 0; i < s.size(); i++) {
            if (indexes.count(s[i]) == 0) {
                indexes[s[i]] = vector<int>();
            }
            indexes[s[i]].push_back(i);
        }
        for (auto& [key, vec] : indexes) {
            intervals.push_back({vec.front(), vec.back()});
        }
        sort(intervals.begin(), intervals.end());
        int minI = intervals[0][0];
        int maxI = intervals[0][1];
        int i = 1;
        while (i < intervals.size()) {
            if (intervals[i][0] > maxI) {
                ans.push_back(maxI - minI + 1);
                minI = intervals[i][0];
                maxI = intervals[i][1];
            }
            else if (intervals[i][0] < maxI) {
                if (intervals[i][1] > maxI) {
                    maxI = intervals[i][1];
                }
            }
            if (i == intervals.size() - 1) {
                ans.push_back(maxI - minI + 1);
            }
            i += 1;
        }
        return ans;
    }
};