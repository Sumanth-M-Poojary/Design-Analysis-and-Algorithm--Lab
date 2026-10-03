def strassen(A,B):
    (a,b),(c,d)=A
    (e,f),(g,h)=B

    p5=(a+b)*(e+h)
    p1=a*(f-h)
    p4=d*(g-e)
    p2=(a+b)*h
    p3=(c+d)*e
    p7=(a-c)*(e+f)
    p6=(b-d)*(g+h)

    return[[-p2+p4+p5+p6    ,p1+p2             ],
           [p3+p4          ,p1-p3+p5-p7]]

def getMat():
    m=[]
    for i in range(2):
        values=input().split()

        row=[]
        for val in values:
            row.append(int(val))

        m.append(row)
    return m

print("Enter Matrix A :")
A=getMat()
print("Enter Matrix B :")
B=getMat()
print("\nProduct is")
print(*strassen(A,B),sep="\n")