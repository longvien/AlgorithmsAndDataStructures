from DSU import DSU
from DSUN import DSUN
# myDSU = DSU()
# graph = [('A', 'B', 1), ('B', 'C', 4), ('C', 'A', 3)]
# print(myDSU.KruskalAlgorithm(graph))

myDSUN = DSUN(7)
graph = [(1, 2, 1), (2, 3, 5), (6, 1, 2)]
print(myDSUN.Kruskal(graph, 4))