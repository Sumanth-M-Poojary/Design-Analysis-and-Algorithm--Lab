class Graph:
    def __init__(self,vertices):
        self.V, self.graph = vertices, []

    def kruskal(self):
        parent={v : v for v in self.V}
        rank={v : 0 for v in self.V}

        def find(i):
            if parent[i] !=i: parent[i] = find(parent[i])
            return parent[i]

        result = []

        for u,v,w in sorted(self.graph,key=lambda x:x[2]):
            rx,ry=find(u),find(v)
            if rx != ry:
                result.append((u,v,w))
                if rank[rx]<rank[ry]:rx,ry=ry,rx
                parent[ry] = rx

                if rank[rx] == rank[ry]:rank[rx]+=1

                if len(result) == len(self.V)-1:break
        return result

vertices=input("Enter the space separated vertices names : ").split()
g=Graph(vertices)

E=int(input("Enter number of edges : "))
print("Enter each edge as source destination weight :  ")

g.graph=[[u,v,int(w)] for u,v,w in (input(f"Edge {i+1} : ").split() for i in range(E))]

mst=g.kruskal()

print("\nEdges in the Minimum spanning Tree: \n"+"-"*45)
for u,v,w in mst:
    print(f"Edge ({u}-{v})\t,Cost : {w}")

print(f"\nTotal Minimum Cost : {sum(w for u,v,w in mst)}")