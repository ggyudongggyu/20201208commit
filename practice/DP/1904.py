import sys
n = int(sys.stdin.readline())
A = {0:0, 1:1}

def fibo_DP(n, A):
    if n in A:
        return A[n]
    A[n] = fibo_DP(n-1, A) + fibo_DP(n-2, A)
    return A[n]

f=fibo_DP(n+1, A)
print(f%15746)
