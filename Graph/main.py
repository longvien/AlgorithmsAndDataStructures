from graphClass import GraphClass
from Grid import Grid
myGraph = GraphClass()
myGraph.addEdge('A', 'B')
myGraph.addEdge('A', 'C')
myGraph.addEdge('B', 'D')
myGraph.addEdge('D', 'C')
myGraph.addEdge('F', 'E')
print('DFS Interactive')
print(myGraph.DFSR())
print('Connected Components Counter Graph')
print(myGraph.componentsCounter())

#examoleGrid
grid = [[1, 0, 1],
        [0, 1, 0],
        [1, 1, 1]
        ]
#exampleGridInADJ
gridADJ = {
    (0,0): [(0,1)],
    (0,1): [(0,0), (1,1)],
    (1,1): [(0,1)],
    (2,0): [],
    (2,2): []
}

myGrid = Grid()
print('Connected Components Counter Grid')
print(myGrid.componentCounterGrid(grid))