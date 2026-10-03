import heapq
from collections import defaultdict

def prims(g,s):
    mst,vis,cost=[],{s},0
    q=[(w,s,n) for n,w in g[s].items()]
    heapq.heapify(q)

    while q:
        w,u,v=heapq.heappop(q)
        if v not in vis:
            vis.add(v); mst.append((u,v,w)); cost+=w
            for n, nw in g[v].items():n not in vis and heapq.heappush(q,(nw,v,n))

    return mst,cost

g=defaultdict(dict)
m=int(input("Enter number of edges : "))
print("Enter edge(Node1 Node2 weight ) : ")
for i in range(m):
    a,b,w=input().split()
    g[a][b]=g[b][a]=float(w)

if g:
    mst,cost=prims(g,next(iter(g)))
    print("\nMinimum Spanning Tree (Edge : weight) : ")
    print("\n".join(f"{a} - {b} : {w}"for a,b, w in mst))
    print(f"Total Minimum Cost : {cost}")