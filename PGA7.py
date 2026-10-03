def getSubset(arr,target,path=[]):
    if target==0: return [path]
    if target<0 or not arr:return []

    return getSubset(arr[1:],target-arr[0],path+[arr[0]])+getSubset(arr[1:],target,path)

s=sorted(list(map(int,input("Enter space-separated positive integers: ").split())))
d=int(input("Enter the target sum: "))
ans=getSubset(s,d)

print("\n".join(f"{{{','.join(map(str,s))}}}"for s in ans) if ans else f"No solution exists for target sum{d}")