import networkx as nx
def dfs(G,startNode):
    stack=[startNode]
    visited=set()

    result=[]

    while stack:
        current=stack.pop()

        if current not in visited:
            visited.add(current)
            result.append(current)

            for neighbor in reversed(list(G.neighbors(current))):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result
G=nx.Graph()

numEdges=int(input("Enter number of edges : "))

print("Enter the nodes of edge : ")
for i in range(numEdges):
    a,b=input().split()
    G.add_edge(a,b)

startNode=input("\nEnter the start node :")
dfsOrder=dfs(G,startNode)
print("DFS Traversal :",dfsOrder)