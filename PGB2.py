def knapsack(capacity, weights,values):
    dp=[0]*(capacity+1)
    chosen=[[]for i in range(capacity+1)]

    for w,v in zip(weights,values):
        for c in range(capacity,w-1,-1):
            if dp[c-w]+v>dp[c]:
                dp[c]=dp[c-w]+v

                chosen[c]=chosen[c-w]+[w]
    return dp[-1],chosen[-1]

cap=int(input("Enter the capacity of knapsack : "))

wts=[int(w) for w in input("Enter space separated weights : ").split()]
vals=[int(v) for v in input("Enter space separated weights : ").split()]

maxval,selwts=knapsack(cap,wts,vals)

print("\n"+"-"*25)
print(f"Maximum value : {maxval}")
print(f"Selected weights : {selwts}")

