N = int(input())
l=[]
for i in range(N):
    l.append(input().split())
l.sort(key=lambda x: int(x[0]))
for i in l:
    print(i[0], i[1])
