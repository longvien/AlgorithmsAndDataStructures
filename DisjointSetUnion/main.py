from DSU import DSU
from DSUN import DSUN
myDSU = DSU()
graph = [('A', 'B', 1), ('B', 'C', 4), ('C', 'A', 3)]
print(myDSU.KruskalAlgorithm(graph))

myDSUN = DSUN(4)
graph = [(1, 2, 1), (2, 3, 5), (3, 1, 2)]
print(myDSUN.KruskalAlgorithm(graph))