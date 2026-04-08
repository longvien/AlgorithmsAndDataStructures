from collections import deque
class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.visited = set()
        self.distance = {} # distance(steps) tracking | for shortest path finding
        self.parent = {} # parent for backtracking | for shortest path finding
        self.queue = deque() # queue for BFS
        self.stack = [] # stack for DFS
        self.directions =  [(1, 0), (-1, 0), (0, 1), (0, -1)] # directions that a cell can travel to
        self.rows = len(self.grid) # number of rows
        self.cols = len(self.grid[0]) # number of columns

    def componentsCounter(self):
        self.visited = set()
        components = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 1 and (r, c) not in self.visited:
                    components += 1
                    self.DFS(r, c)
        return components

    def DFS(self, r, c):
        if 0 > r or r >= self.rows or 0 > c or c >= self.cols:
            return
        if (r, c) in self.visited:
            return
        if self.grid[r][c] == 0:
            return
        if self.grid[r][c] == 1:
            self.visited.add((r, c))
            self.DFS(r + 1, c)
            self.DFS(r - 1, c)
            self.DFS(r, c + 1)
            self.DFS(r, c - 1)
        return self.visited

    def BFS(self, sr, sc, tr, tc):
        self.queue = deque()
        self.visited = set()
        self.parent = {}
        self.distance = {}
        backTrack = []
        if 0 > sr or sr >= self.rows or 0 > sc or sc >= self.cols or 0 > tr or tr >= self.rows or 0 > tc or tc >= self.cols:
            raise IndexError("Index out of range")
        elif self.grid[sr][sc] == 0 or self.grid[tr][tc] == 0:
            print("Invalid starting/ ending point!")
            return 0
        else:
            self.visited.add((sr, sc))
            self.distance[(sr, sc)] = 0
            self.queue.append((sr, sc))
            while self.queue:
                r, c = self.queue.popleft()
                if r == tr and c == tc:
                    print(self.distance[(r, c)])
                    while self.parent[(r, c)] != (sr, sc):
                        backTrack.append(self.parent[(r, c)])
                        r, c = self.parent[(r, c)]
                    backTrack.append((sr, sc))
                    backTrack.reverse()
                    backTrack.append((tr, tc))
                    return backTrack
                else:
                    for dr, dc in self.directions:
                        nr = r + dr
                        nc = c + dc
                        if 0 > nr or nr >= self.rows or 0 > nc or nc >= self.cols or self.grid[nr][nc] != 1:
                            continue
                        else:
                            if (nr, nc) not in self.visited:
                                self.visited.add((nr, nc))
                                self.distance[(nr, nc)] = self.distance[(r, c)] + 1
                                self.parent[(nr, nc)] = (r, c)
                                self.queue.append((nr, nc))
                            else:
                                continue
            raise Exception("No path to destination Found")

    def DFSI(self, sr, sc, tr, tc):
        self.stack = []
        self.visited = set()
        self.distance = {}

        if 0 > sr or sr >= self.rows or 0 > sc or sc >= self.cols or 0 > tr or tr >= self.rows or 0 > tc or tc >= self.cols:
            raise IndexError("Index out of range")
        elif self.grid[sr][sc] == 0 or self.grid[tr][tc] == 0:
            print("Invalid starting/ ending point!")
            return 0
        else:
            self.visited.add((sr, sc))
            self.stack.append((sr, sc))
            self.distance[(sr, sc)] = 0
            while len(self.stack) > 0:
                current = self.stack.pop()
                if current[0] == tr and current[1] == tc:
                    return self.distance[(current[0], current[1])]
                for dr, dc in self.directions:
                    nr = current[0] + dr
                    nc = current[1] + dc
                    if 0 > nr or nr >= self.rows or 0 > nc or nc >= self.cols or self.grid[nr][nc] != 1:
                        continue
                    else:
                        if (nr, nc) not in self.visited:
                            self.visited.add((nr, nc))
                            self.stack.append((nr, nc))
                            self.distance[(nr, nc)] = self.distance[(current[0], current[1])] + 1
                        else:
                            continue
            raise Exception("No path to destination Found")

    def multiSourceBFS(self, sourceNode):
        rows = len(self.grid)
        cols = len(self.grid[0])
        distance = [[float("inf") for i in range(cols)] for i in range(rows)] # create 'rows' rows in distance. For each index in each rows initialize it to infinity.
        self.queue = deque()
        self.visited = set()
        for r in range(rows):
            for c in range(cols):
                if self.grid[r][c] == sourceNode:
                    distance[r][c] = 0
                    self.queue.append((r, c))
                    self.visited.add((r, c))
        while self.queue:
            r, c = self.queue.popleft()
            for dr, dc in self.directions:
                nr = dr + r
                nc = dc + c
                if 0 > nr or nr >= rows or 0 > nc or nc >= cols or (nr, nc) in self.visited:
                    continue
                distance[nr][nc] = distance[r][c] + 1
                self.queue.append((nr, nc))
                self.visited.add((nr, nc))
        return distance


