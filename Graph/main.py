from graphClass import GraphClass

myGraph = GraphClass()
myGraph.addEdge('A', 'B')
myGraph.addEdge('A', 'C')
myGraph.addEdge('B', 'D')
myGraph.addEdge('D', 'C')
myGraph.addEdge('F', 'E')
for i in myGraph.DFSInterative():
    print(i)
print(myGraph.componentsCounter())