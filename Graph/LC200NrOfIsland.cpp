#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<bool>> v; 
    int m, n;
    void dfs(int r, int c, vector<vector<char>>& grid) {
        if (v[r][c] != 0 || grid[r][c] == '0') return;
        vector<pair<int, int>> dir = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
        v[r][c] = 1;
        for (auto [dr, dc] : dir) {
            int nr = r + dr, nc = c + dc;
            if (0 > nr || nr >= m || 0 > nc || nc >= n) continue;
            dfs(nr, nc, grid);
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        m = grid.size(), n = grid[0].size();
        v = vector<vector<bool>>(m, vector<bool>(n));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1' && v[i][j] == 0) {
                    count++;
                    dfs(i, j, grid);
                }
            }
        }
        return count;
    }
};