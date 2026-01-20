# Breadth First Search Implementation in Python

from queue import Queue
adjMatrix = [[0,1,1,0] , [1,0,1,1] , [1,1,0,0] , [0,1,0,0]]
def bfs(adjmatrix , src):

    nodes = Queue()
    vis = dict()
    nodes.put(src)
    nodes.put(None)

    while True:
        currNode = nodes.get()

        if currNode is None:
            if nodes.empty():
                break
            print()
            nodes.put(None)
            continue

        print(currNode , end = " ")
        vis[currNode] = 1
        for i in range(len(adjmatrix)):
            if adjmatrix[currNode-1][i] == 1 and vis.get(i+1) != 1:
                nodes.put(i+1)
                vis[i+1] = 1
                

bfs(adjMatrix , 1)
