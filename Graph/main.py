from graphClass import unDirectedGraph
from Grid import Grid
from graphDirectedClass import DirectedGraph
print("Normal Graph:")
myGraph = unDirectedGraph()

myGraph.addUndirectedEdge('A', 'B')
myGraph.addUndirectedEdge('A', 'C')
myGraph.addUndirectedEdge('B', 'D')
myGraph.addUndirectedEdge('D', 'C')
myGraph.addUndirectedEdge('F', 'E')
print('DFS Recursive')
print(myGraph.DFSR())
print("                                      ")
print('Connected Components Counter Graph')
print(myGraph.componentsCounter())
print("                                      ")
print("Dijkstra Algorithm")
print(myGraph.DijkstraAlgorithm('A', 'B'))
print("                                      ")
print("                                      ")
print("Grid")
#exampleGrid
grid = [['S', 0, 0, 0],
        [0, 0, 'S', 0],
        [0, 0, 0, 0]
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
print("                                      ")
print('BFS Grid/ Shortest Path finding on unweighted Graph/Grid')
print('Shortest Path:', myGrid.BFS(0, 0, 2, 3))
print("                                      ")
print("Multi Source BFS")
print(myGrid.multiSourceBFS('S'))

# #directedGraphCycleDetection
myDirectedGraph = DirectedGraph()
myDirectedGraph.addEdges('a', 'b')
myDirectedGraph.addEdges('a', 'c')
myDirectedGraph.addEdges('b', 'd')
myDirectedGraph.addEdges('c', 'd')
myDirectedGraph.addEdges('d', 'e')
myDirectedGraph.addEdges('b', 'e')

print("                                      ")
print("Directed Graph Cycle Detector")
print(myDirectedGraph.cycleDetector())

print("                                      ")
print("Directed Graph Components Counter")
print(myDirectedGraph.componentsCounter())

print("                                      ")
print("Topological Sort")
print(myDirectedGraph.topologicalSort())

print("                                      ")
print("Kahn's Algorithm")
print(myDirectedGraph.KahnAlgorithm())