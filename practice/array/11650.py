# from operator import itemgetter

N = int(input())
list = []
for i in range(N):
    list.append(tuple(map(int, input().split())))
list.sort()
# list.sort(key=itemgetter(0,1))
for i in list:
    print(*i)
#
# N = int(input())
# list = []
# for i in range(N):
#     list.append(list(map(int, input().split())))
#
# list.sort()
# for i in list:
#     print(i[0], i[1])
