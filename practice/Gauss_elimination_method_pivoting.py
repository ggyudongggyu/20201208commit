import numpy as np

n=int(input('Write the size of matrix A : '))
A=np.zeros(shape(n, n+1),dtype = float)

for i in range(n):
    for j in range(n+1):
        A[i,j] = float(input())

for i in range(0, n-1):
    for j in range(i+1, n):
        if A[i,j] != 0 :
            temp = A[j,i]/A[i,i]
            A[j,:] = A[j,:] - temp * A[i,:]

print(np.matrix(A))