#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O3")
#define fi first
#define se second

class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        if (grid[0][0] == 1 || grid[n-1][n-1] == 1) {return -1;}
        vector<pair<int, int>> dir = {{-1,0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}};
        vector<vector<int>> ans(n, vector<int>(n, -1));
        ans[0][0] = 1;
        queue<pair<int, int>> q;
        q.push({0, 0});
        bool found = false;
        while (!q.empty() && !found) {
            int r = q.front().fi;
            int c = q.front().se;
            q.pop();
            for (const auto& [dr, dc] : dir) {
                int nr = r + dr;
                int nc = c + dc;
                if (0 > nr || nr >= n || 0 > nc || nc >= n || grid[nr][nc] == 1 || ans[nr][nc] != -1) {continue;}
                ans[nr][nc] = ans[r][c]+1;
                if (nr == n-1 && nc == n-1) {
                    found = true;
                    break;
                }
                q.push({nr, nc});
            }
        }
        return ans[n-1][n-1];
    }
};