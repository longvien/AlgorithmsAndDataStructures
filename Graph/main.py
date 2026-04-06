from graphClass import unDirectedGraph
from Grid import Grid
from graphDirectedClass import directedGraph
print("Normal Graph:")
print("=======================================")
myGraph = unDirectedGraph()

myGraph.addUndirectedEdge('A', 'B')
myGraph.addUndirectedEdge('A', 'C')
myGraph.addUndirectedEdge('B', 'D')
myGraph.addUndirectedEdge('D', 'C')
myGraph.addUndirectedEdge('F', 'E')
print('DFS Recursive')
print(myGraph.DFSR())
print("=------------------------------------=")
print('Connected Components Counter Graph')
print(myGraph.componentsCounter())
print("Dijkstra Algorithm")
print(myGraph.DijkstraAlgorithm('A', 'B'))
print("=======================================")
print("Grid")
#exampleGrid
grid = [[1, 1, 1, 1],
        [0, 1, 1, 1],
        [0, 0, 0, 1]
        ]
#exampleGridInADJ
gridADJ = {
    (0,0): [(0,1)],
    (0,1): [(0,0), (1,1)],
    (1,1): [(0,1)],
    (2,0): [],
    (2,2): []
}

myGrid = Grid(grid)
print('Components Counter')
print(myGrid.componentsCounter())
print("=------------------------------------=")
print('BFS Grid/ Shortest Path finding on unweighted Graph/Grid')
print('Shortest Path:', myGrid.BFS(0, 0, 2, 3))
print("=------------------------------------=")
print('DFS Grid')
print(myGrid.DFSI(0, 0,2, 3))
print("=======================================")

print("Directed Graph Cycle Detection")
#directedGraphCycleDetection
directed = directedGraph()


directed.addDirectedEdge('a', 'b')
directed.addDirectedEdge('b', 'c')
directed.addDirectedEdge('c', 'a')

print(directed.cycleDetector())
print("=======================================")
print("Topo Sort, Kahn's Algorithm")
print("=------------------------------------=")
print("Directed Graph Topological Sort")
print(directed.topologicalSort())

print("=------------------------------------=")
# Kahn's Algorithm
print("Kahn's Algorithm")
print(directed.kahnAlgorithm())
print("=======================================")