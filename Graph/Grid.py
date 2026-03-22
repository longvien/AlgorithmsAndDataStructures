grid = [[1, 0, 1],
        [0, 1, 0],
        [1, 1, 1]
        ]

visited = set()
def componentCounterGrid(self):
    counter = 0
    row = len(


def DFSGrid(r, c):
    rows = len(grid)
    cols = len(grid[0])
    if 0 > r or r >= rows or  0 > c or c >= cols:
        return
    if (r, c) in visited:
        return
    if grid[r][c] == 0:
        return
    if grid[r][c] == 1:
        visited.add((r, c))
        DFSGrid(r + 1, c)
        DFSGrid(r - 1, c)
        DFSGrid(r, c + 1)
        DFSGrid(r, c - 1)
    return visited



gridADJ = {
    (0,0): [(0,1)],
    (0,1): [(0,0), (1,1)],
    (1,1): [(0,1)],
    (2,0): [],
    (2,2): []
}