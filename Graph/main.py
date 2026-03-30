from graphClass import unDirectedGraph
from Grid import Grid
from graphDirectedClass import directedGraph
myGraph = unDirectedGraph()
myGraph.addUndirectedEdge('A', 'B')
myGraph.addUndirectedEdge('A', 'C')
myGraph.addUndirectedEdge('B', 'D')
myGraph.addUndirectedEdge('D', 'C')
myGraph.addUndirectedEdge('F', 'E')
print('DFS Recursive')
print(myGraph.DFSR())
print('Connected Components Counter Graph')
print(myGraph.componentsCounter())

#examoleGrid
grid = [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
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
print('BFS Grid')
print(myGrid.BFS(0, 0, grid, 2, 2))


#directedGraphCycleDetection
directed = directedGraph()

directed.addDirectedEdge('b', 'c')
directed.addDirectedEdge('a', 'c')

directed.addDirectedEdge('b', 'd')
directed.addDirectedEdge('c', 'e')
directed.addDirectedEdge('d', 'e')

print("Directed Graph Topological Sort")
print(directed.topologicalSort())

# Kahn's Algorithm

print("Kahn's Algorithm")
print(directed.kahnAlgorithm())