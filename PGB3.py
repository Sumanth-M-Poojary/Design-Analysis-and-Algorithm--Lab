def tsp(graph,start=0):
    unvisited=set(range(len(graph)))-{start}
    path,dist,curr=[start],0,start

    while unvisited:
        nxt=min(unvisited,key=lambda c: graph[curr][c])
        path.append(nxt)
        dist,curr=dist+graph[curr][nxt],nxt
        unvisited.remove(nxt)

    return path+[start],dist+graph[curr][start]
n=int(input("Enter number of cities : "))
print("Enter space separated distances - row by row : ")

mat=[[float(x) for x in input(f"City {i} : ").split()]for i in range(n)]
starcity=int(input("Enter start city  : "))
path,distance=tsp(mat,starcity)

print(f"\n-----Result-----\nPath : {path}\nDistance : {distance}")

    