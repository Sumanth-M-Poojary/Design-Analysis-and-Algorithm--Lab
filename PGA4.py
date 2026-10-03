import networkx as nx

def bfs(G,startNode):
    visited=set()
    queue=[startNode]
    visited.add(startNode)

    result=[]

    while queue:
        current=queue.pop(0)
        result.append(current)

        for neighbor in G.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

G=nx.Graph()    
numEdges=int(input("Enter number of edges: "))

print("Enter the nodes of a edge: ")
for i in range(numEdges):
    a,b=input().split()
    G.add_edge(a,b)

startNode=input("\nEnter the starting node : ")
bfsOrder=bfs(G,startNode)

print("BFS  Traversal : ",bfsOrder)