from operator import itemgetter

N = int(input())
list = []
for i in range(N):
    list.append(tuple(map(int, input().split())))
list.sort(key=itemgetter(1,0))
for i in list:
    print(*i)

# n = int(input())
# s = [list(map(int,input().split())) for i in range(n)]
# s.sort(key=lambda x:(x[1],x[0]))
#
# for i in s:
#     print(*i)
