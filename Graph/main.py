from graphClass import GraphClass

myGraph = GraphClass()
myGraph.addEdge('A', 'B')
myGraph.addEdge('A', 'C')
myGraph.addEdge('B', 'D')
myGraph.addEdge('D', 'C')
print(myGraph.DFSInteractive())