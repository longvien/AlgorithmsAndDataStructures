class Solution:
    def __init__(self):
        self.visited = set()
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.valid = True

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        count = 0
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if (r, c) not in self.visited and grid2[r][c] == 1 and grid1[r][c] == 1:
                    self.valid = True
                    self.dfs(r, c, grid2, grid1)
                    if self.valid:
                        count += 1
        return count

    def dfs(self, r, c, grid2, grid1):
        self.visited.add((r, c))
        if grid1[r][c] == 0: self.valid = False
        for dr, dc in self.directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid2) and 0 <= nc < len(grid2[0]) and (nr, nc) not in self.visited and grid2[nr][nc] == 1:
                self.dfs(nr, nc, grid2, grid1)
            else:
                continue