class Grid:
    def __init__(self):
        self.visited = []
        self.distance = {}
        self.parent = {}
        self.queue = []
        self.stack = []
    def componentCounterGrid(self, grid):
        counter = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in self.visited:
                    counter += 1
                    self.DFS(r, c, grid)
        return counter


    def DFS(self, r, c, grid):
        rows = len(grid)
        cols = len(grid[0])
        if 0 > r or r >= rows or  0 > c or c >= cols:
            return
        if (r, c) in self.visited:
            return
        if grid[r][c] == 0:
            return
        if grid[r][c] == 1:
            self.visited.append((r, c))
            self.DFS(r + 1, c, grid)
            self.DFS(r - 1, c, grid)
            self.DFS(r, c + 1, grid)
            self.DFS(r, c - 1, grid)
        return self.visited

    def BFS(self, sr, sc, grid, tr, tc):
        self.queue = []
        self.visited = []
        self.parent = {}
        self.distance = {}

        rows = len(grid)
        cols = len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        if 0 > sr or sr >= rows or 0 > sc or sc >= cols or 0 > tr or tr >= rows or 0 > tc or tc >= cols:
            raise IndexError("Index out of range")
        else:
            self.visited.append((sr, sc))
            self.distance[(sr, sc)] = 0
            self.queue.append((sr, sc))
            while len(self.queue) > 0:
                current = self.queue.pop(0)
                if current[0] == tr and current[1] == tc:
                    return self.distance[(current[0], current[1])]
                else:
                    for dr, dc in directions:
                        nr = current[0] + dr
                        nc = current[1] + dc
                        if 0 > nr or nr >= rows or 0 > nc or nc >= cols or grid[nr][nc] == 1:
                            continue
                        else:
                            if (nr, nc) not in self.visited:
                                self.visited.append((nr, nc))
                                self.distance[(nr, nc)] = self.distance[(current[0], current[1])] + 1
                                self.parent[(nr, nc)] = (current[0], current[1])
                                self.queue.append((nr, nc))
                            else:
                                continue
    def DFSI(self, sr, sc, grid):
        self.stack = []
        self.visited = []

        rows = len(grid)
        cols = len(grid[0])

        if 0 > sr or sr >= rows or 0 > sc or sc >= cols:
            raise IndexError("Index out of range")












