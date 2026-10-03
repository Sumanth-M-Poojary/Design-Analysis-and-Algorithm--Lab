def sort(a):
    for i in range(1,len(a)):
        k,j=a[i],i-1
        while j>=0 and k<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=k

arr=list(map(int,input("Enter space seprated number").split()))
print("Original list: ",arr)
sort(arr)
print("Sorted list: ",arr)