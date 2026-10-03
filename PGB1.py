import random, time

def msort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    L,R=msort(arr[:mid]),msort(arr[mid:])

    res,i,j=[],0,0
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            res.append(L[i])
            i+=1
        else:
            res.append(R[j])
            j+=1
    return res+L[i:]+R[j:]

values=[5001,10000,25000,50000,100000,150000]

recordTime={}
for n in values:
    arr=[random.randint(1,1000) for x in range(n)]
    start=time.time()
    msort(arr)
    end=time.time()
    recordTime[n]=end-start

print(f"{'n Elements ':<12}|Time Taken (s)")
print('-'*28)
for n,t in recordTime.items():
    print(f"{n:<12}|{t:.5f}")