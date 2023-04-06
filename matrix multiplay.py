#matrix
A=[[5,3,2],[6,8,4]]
B=[[4,5],[9,2],[5,7]]
if len (B)== len (A[0]):
    c= [[0,0],[0,0]]
    for s in range (len(B[0])):
        for i in range (len(A)):
            e=0
            for j in range (len(A[0])):
                d=A[i][j]*B[j][s]
                e=d+e
            c[i][s]=e
    print(c)
else:
    print("not possible")
    
