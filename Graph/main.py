from UDGraph import UndirectedGraph
from DGraph import DirectedGraph
from Grid import Grid

def main():
    myUDG = UndirectedGraph()
    myUDG.addEdges('a', 'b')
    myUDG.addEdges('a', 'c')
    myUDG.addEdges('b', 'd')
    myUDG.addEdges('z', 'g')
    print("Undirected Graph")
    print(f"DFS Recursive: {myUDG.DFSR()}")
    print(f"DFS Interactive: {myUDG.DFS()}")
    print(f"BFS: {myUDG.BFS()}")
    print(f"Components Counter: {myUDG.componentsCounter()}")
    print(f"Cycle Detector: {myUDG.cycleDetector()}")
    # print(f"Dijktra's Algorithm: {myUDG.DijkstraAlgorithm('A')}")

    print("                            ")
    myDG = DirectedGraph()
    myDG.addEdges('a', 'b')
    myDG.addEdges('b', 'd')
    myDG.addEdges('b', 'c')
    myDG.addEdges('d', 'e')
    myDG.addEdges('c', 'g')

    print("Directed Graph")
    print(f"DFS Recursive: {myDG.DFSR()}")
    print(f"DFS Interactive: {myDG.DFS()}")
    print(f"BFS: {myDG.BFS()}")
    print(f"Components Counter: {myDG.componentsCounter()}")
    print(f"Cycle Detector: {myDG.cycleDetector()}")
    print(f"Topological Sort DFS based: {myDG.topologicalSort()}")
    print(f"Kahn's Algorithm (Topological Sort BFS based): {myDG.KahnAlgorithm()}")

    print("                            ")
    grid = [[1, 1, 1],
            [6, 0, 6],
            [1, 1, 1]]
    myGrid = Grid(grid)
    print("Grid")
    print(f"DFS: {myGrid.DFSR(0,0)}")
    #print(f"Shortest Path BFS: {myGrid.BFSShortestPath(0, 0, 2, 2)}")
    sources = [6]
    print(f"Multi Source BFS: {myGrid.MultiSourceBFS(sources)}")

if __name__ == "__main__":
    main()