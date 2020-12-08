from operator import itemgetter

N = int(input())
a = []
for i in range(N):
    s = str(input())
    s_len = len(s)
    a.append((s, s_len))

a = list(set(a))
a.sort(key=itemgetter(1,0))
for i in a:
    print(i[0])
