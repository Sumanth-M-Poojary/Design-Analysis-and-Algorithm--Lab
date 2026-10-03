def minmax(arr,L,h):
    if L==h:
        return arr[L],arr[L]
    if L+1==L:
        return (arr[L],arr[h] if arr[L]<arr[h] else(arr[h],arr[L]))

    mid=(L+h)//2
    lmin, lmax =minmax(arr,L,mid)
    rmin,rmax=minmax(arr,mid+1,h)

    return min(lmin,rmin),max(lmax,rmax)

n=int(input("Enter total number of element : "))
arr=list(map(int,input(f"Enter {n} number: ").split()))[:n]

minval,maxval=minmax(arr,0,len(arr)-1)
print(f"Minimum : {minval} \nMaximum : {maxval}")