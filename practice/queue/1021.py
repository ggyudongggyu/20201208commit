n, m = map(int, input().split())
s = list(map(int, input().split()))
q = [i for i in range(1, n+1)]
cnt = 0

for i in range(m):
    index = q.index(q[i])
    leng = len(q)
    if index < leng - index :
        while True:
            if q[0]==s[i]:
                del q[0]
                break
            else:
                q.append(q[0])
                del q[0]
                cnt += 1
            
    else:
        while True:
            if q[0] ==s[i]:
                del q[0]
                break
            else:
                q.append(q[-1])
                q.pop()
                cnt += 1
            
print(cnt)
print(s)
print(q)