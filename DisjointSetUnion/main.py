from DSU import DSU
myDSU = DSU()
graph = [('A', 'B', 1), ('B', 'C', 4), ('C', 'A', 3)]
print(myDSU.KruskalAlgorithm(graph))
