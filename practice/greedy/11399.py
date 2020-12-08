__sum__=0
N= int(input())
A = list(map(int, input().split()))
A.sort()

for i in range(N):
    __sum__ = __sum__ + sum(A)
    if len(A)>0:
        A.pop()
print(__sum__)
