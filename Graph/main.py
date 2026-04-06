from graphClass import unDirectedGraph
from Grid import Grid
from graphDirectedClass import DirectedGraph
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
print('BFS Grid/ Shortest Path finding on unweighted Graph/Grid')
print('Shortest Path:', myGrid.BFS(0, 0, 2, 3))
print('DFS Grid')
print(myGrid.DFSI(0, 0,2, 3))

print("--------------------------------------")
print("Directed Graph Cycle Detection")
#directedGraphCycleDetection
myDirectedGraph = DirectedGraph()
myDirectedGraph.addEdges('a', 'b')
myDirectedGraph.addEdges('a', 'c')
myDirectedGraph.addEdges('b', 'd')
myDirectedGraph.addEdges('c', 'd')
myDirectedGraph.addEdges('d', 'e')
myDirectedGraph.addEdges('b', 'e')

print("Directed Graph Cycle Detector")
print(myDirectedGraph.cycleDetector())

print("Directed Graph Components Counter")
print(myDirectedGraph.componentsCounter())

print("Topological Sort")
print(myDirectedGraph.topologicalSort())

print("Kahn's Algorithm")
print(myDirectedGraph.KahnAlgorithm())