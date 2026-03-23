class Grid:
    def __init__(self):
        self.visited = set()

    def componentCounterGrid(self, grid):
        counter = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in self.visited:
                    counter += 1
                    self.DFSGrid(r, c, grid)
        return counter


    def DFSGrid(self, r, c, grid):
        rows = len(grid)
        cols = len(grid[0])
        if 0 > r or r >= rows or  0 > c or c >= cols:
            return
        if (r, c) in self.visited:
            return
        if grid[r][c] == 0:
            return
        if grid[r][c] == 1:
            self.visited.add((r, c))
            self.DFSGrid(r + 1, c, grid)
            self.DFSGrid(r - 1, c, grid)
            self.DFSGrid(r, c + 1, grid)
            self.DFSGrid(r, c - 1, grid)
        return self.visited


