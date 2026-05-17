from collections import deque
class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.visitedSet = set()
        self.visited = []
        self.queue = deque()
        self.directions = [(0, 1), (0, -1), (1, 0), (-1,  0)]

    def DFSR(self, r, c):
        if 0 > r or r >= self.rows or 0 > c or c >= self.cols: raise Exception("Position out of range")
        if self.grid[r][c] == 0: raise Exception("Invalid Position")
        self.visitedSet = set()
        self.visited = []
        self._DFSR(r, c)
        return self.visited

    def _DFSR(self, r, c):
        if 0 > r or r >= self.rows or 0 > c or c >= self.cols: return
        if (r, c) in self.visitedSet: return
        if self.grid[r][c] == 0: return
        if self.grid[r][c] == 1:
            self.visitedSet.add((r, c))
            self.visited.append((r, c))
            for dr, dc in self.directions:
                nr = dr + r
                nc = dc + c
                self._DFSR(nr, nc)

    def componentsCounter(self):
        self.visitedSet = set()
        counter = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) not in self.visitedSet and self.grid[r][c] == 1:
                    counter += 1
                    self._componentsCounter(r, c)
        return counter
    def _componentsCounter(self, r, c):
        if (r, c) in self.visitedSet or 0 > r or r >= self.rows or 0 > c or c >= self.cols or self.grid[r][c] == 0:
            return
        if self.grid[r][c] == 1:
            self.visitedSet.add((r, c))
            for dr, dc in self.directions:
                nr = dr + r
                nc = dc + c
                self._componentsCounter(nr, nc)


    def BFSShortestPath(self, r, c, ar, ac):
        if 0 > r or r >= self.rows or 0 > c or c >= self.cols or 0 > ar or ar >= self.rows or 0 > ac or ac >= self.cols: raise Exception("Position out of range")
        if self.grid[r][c] == 0 or self.grid[ar][ac] == 0: raise Exception("Invalid Position")
        distance = {}
        parent = {}
        self.queue = deque()
        self.visitedSet = set()
        self.queue.append((r, c))
        self.visitedSet.add((r, c))
        distance[(r, c)] = 0
        parent[(r, c)] = None
        while self.queue:
            r, c = self.queue.popleft()
            if r == ar and c == ac:
                solution = []
                current = (r , c)
                while current is not None:
                    solution.append(current)
                    current = parent[(current[0], current[1])]
                solution.reverse()
                print(f"Shortest Distance: {distance[(r, c)]}")
                return solution
            for dr, dc in self.directions:
                nr = dr + r
                nc = dc + c
                if (nr, nc) in self.visitedSet or 0 > nr or nr >= self.rows or 0 > nc or nc >= self.cols or self.grid[nr][nc] != 1:
                    continue
                self.queue.append((nr, nc))
                self.visitedSet.add((nr, nc))
                distance[(nr, nc)] = distance[(r, c)] + 1
                parent[(nr, nc)] = (r, c)
        raise Exception("Destination not reachable")

    def MultiSourceBFS(self, sources):
        self.queue = deque()
        self.visitedSet = set()
        distance = [[float("inf") for i in range(self.cols)] for i in range(self.rows)]

        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] in sources:
                    distance[r][c] = 0
                    self.queue.append((r, c))
                    self.visitedSet.add((r, c))
        while self.queue:
            r, c = self.queue.popleft()
            for dr , dc in self.directions:
                nr = dr + r
                nc = dc + c
                if 0 > nr or nr >= self.rows or 0 > nc or nc >= self.cols or self.grid[nr][nc] == 0 or (nr ,nc) in self.visitedSet or self.grid[nr][nc] == 0:
                    continue
                distance[nr][nc] = distance[r][c] + 1
                self.visitedSet.add((nr, nc))
                self.queue.append((nr, nc))
        return distance


