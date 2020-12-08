import collections


# A = [[0 for col in range(10)] for row in range(10)]
#
# for i in range(10):
#     for j in range(10):
#         A[i][j] = i * j
#
# for j in range(len(A)):
#     print(A[j], end="\n")

##################################

# if 0:
#     print("True")
# else: print("False")

###########
# import random
# print(random.randrange(1,7))
##########

# try :
#     a = 10 / 0
# except ZeroDivisionError as ex:
#     print(ex)
#     print(type(ex))
#     print(ex.args)
# else:
#     print('completed')

#####################################

# A=[]
# for i in range(1, 101):
#     A.append(i)
# # A.reverse()
# # print(A)

###################

# import random
# random.seed(1)
# A=[]
# for i in range(1, 30) :
#     B = random.randrange(1,20)
#     A.append(B)
# print(A)

###################

# location = {
# 'Prefectur': 'hokkaido',
# 'city': 'wakananai',
# 'latitude': '45.404',
# 'longitute': '141.68'
# }
# location['city'] = 'wakkanai'
# location['population']= 40151
# if 'Sity'in location:
#     print(location['city'])

##############

# wday = ['Sun', 'Man','Tue','Wed','Thu','Fri']
# wday[1] = 'Mon'
# wday.append('Sat')
# idx = len(wday) - 2
# print(wday[idx])

####

# def spam(num):
#     return 'Spam'*num
# order1 = spam(3)
# order2 = spam(1)
# print(order1 + order2)

# class Spam:
#     def manufacture(self):
#         print('Homel Foods Cooporation')
# lunch = Spam()
# Company = lunch.manufacture()
# print(Company)

###############

# try:
#     c = 1//9
#     a = 10/0
# except TypeError:
#     print('Type ERROR')
# except ZeroDivisionError:
#     print('ZeroDiv ERORR')
# except:
#     print('ERROR')

##########
# class Spam:
#     def __init__(self, amount, salt):
#         self.salt = salt
#         self.amount = amount
#     def __str__(self):
#         msg1 = str(self.amount) + ' gram'
#         msg2 = str(self.salt) + ' milligrams'
#         return msg1 + ', ' + msg2

# lunch = Spam(280,560)
# print(lunch)

####

# print("{0:f}".format(12.34))
##

# f1 = 'cat'
# f0= 'rabbit'
# print('The quick brown {1} jumps over the lazy{0}'.format('fow', 'dog'))

# sentence = 'The quick brown fox, jumps over the lazy dog'
# sentences = sentence.split(',')
# words = sentences[1].split(' ')
# print(words[-1].title())

# import datetime
# from datetime import date
# # print(datetime.date.today())
# print(date.today())

# rabbits = ['Flopsy','Mopsy','Peter','Lily','Cotton-tail']
# trap = ",".join(rabbits)
# print(trap.split(',')[2])

# with open('sample.txt') as fin:
#     contents = fin.readline()
# if fin.closed:
#     print('something else')
# else:
#     print('none')

# import re
# m = re.search(r'You', 'Young Sharlock')
# if m :
#     print('hit')
# else:
#     print('miss')

# peter_rabbit = ['Flopsy','Mopsy','Peter','Lily','Cotton-tail']
# watership_down = ['Bigwig','Fiver','Hazle','Clover','Hyzenthlay']

# for i in range(len(watership_down)):
#     if i == 3 :
#         print(peter_rabbit[i], 'and', watership_down[i])



#######################


# class japanese:
#     def __init__(self, ninzu, namae):
#         self.name = namae
#         print("こんにちは",self.name,"です。")
#         self.pop = ninzu
#         print("日本の人数は",self.pop,"です。")

# class korean:
#     def __init__(self, ingu, irum):
#         self.name = irum
#         print("안녕하세요", self.name,"입니다.")
#         self.pop = ingu
#         print("한국의 인구는",self.pop,"입니다")


# soneshin = japanese(127185000, 'sonehara')
# shimizu  = japanese(1221, 'masaki')
# park = korean(60000000, 'donggyu')

# print(soneshin,'\n',park)

# a = [1,10,2,3,4,5,6]
# print(max(a))
# print(max )

# sentence = "Hello, my name is minori"
# print(sentence.split(',',3 #list[3]まで作る予定です))

# n=int(input())
# for i in range(1, n+1):
#     print("*"*i)
# for j in range(n-1, 0, -1):
#     print("*"*j)


# A = [2]
# A += [3]
# print(A)


# a, b = map(float, input().split())
# print(a/b)


# case = int(input())
# a = list(input())
# len = len(a)
#
# for i in range(case-1):
#     b = list(input())
#     for j in range(len):
#         if a[j]!=b[j]:
#             a[j]="?"
# print("".join(a))

# case = int(input())
# list = [[10] , [1], [2,4,8,6], [3,9,7,1], [6,4], [5], [6] ,[7,9,3,1], [8,4,2,6],[1,9]]
# for _ in range(case):
#     a, b = map(int, input().split())
#     a %= 10
#     if a==1 or a==5 or a==6 or a==0:
#         print(list[a][0])
#     elif a==4 or a==9:
#         print(list[a][b%2])
#     else:
#         print(list[a][b%4-1])


# N = int(input())
# cnt = 0
# M = N
# while True:
#     a, b = M//10, M%10
#     c = a+b
#     M = 10*b + (c%10)
#     cnt+=1
#     if M==N:
#         break
# print(cnt)


# a, b = map(int, input().split())
# if a*b > 0:
#     print(abs(a-b))
# else:
#     print(abs(a)+abs(b))


#==================달팽이 문제==========================
# step = 1 # 증가/감소 크기: 1, -1
# x = 0    # 줄 위치
# y = -1   # 칸 위치 (배열 선두보다 한칸 앞)
# size = int(input()) # 배열 크기 (5*5 배열)
# k = int(input())
# n = size**2 + 1    # 숫자 1, 2, 3, ...
# arr = [[0]*size for i in range(size)]   # 2차원 배열 구조
#
# while True:
#     for _ in range(size):  # 몇 칸 진행할까
#         n -= 1
#         y += step
#         arr[y][x] = n
#         if arr[y][x] == k :
#             ry = y + 1
#             rx = x + 1
#     size -= 1
#     if size < 1:  # 출력할 게 없으면 종료
#         break
#     for _ in range(size):  # 몇 줄 진행할까
#         n -= 1
#         x += step
#         arr[y][x] = n
#         if arr[y][x] == k :
#             ry = y + 1
#             rx = x + 1
#     step = -step  # 증감 방향을 반대로
#
# for i in arr:
#     for j in i:
#         print(j, end=' ')
#     print()
# print(ry, rx)
#============================================
#
# cnt = [0, 31, 28, 31, 30,31,30,31,31,30,31,30,31]
# ans = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
# m, d = map(int, input().split())
# sum=0
# for i in range(m):
#     sum += cnt[i]
# sum += d
# print(ans[sum%7])



# case = int(input())
# for _ in range(case):
#     a, b = map(int, input().split())
#     if a>=b:
#         A, B = a, b
#     else: A, B = b, a
#     if A&B==0:
#         print(A)
#     else:


# from math import gcd
#
# def lcm(x, y):
#     return x*y // gcd(x,y)
#
# case = int(input())
# for _ in range(case):
#     a, b = map(int, input().split())
#     print(lcm(a,b))

#
# n = int(input())
# if n==0:
#     print(n)
# else:
#     x = 0
#     cnt = 0
#     while n>0:
#         e = 8 ** cnt
#         x += (n % 10) * e
#         n //= 10
#         cnt += 1
#     res = []
#     while x>0:
#         res.append(x%2)
#         x //= 2
#     for i in range(len(res)-1, -1, -1):
#         print(res[i], end='')
#
#
# x = int(input(), 8)
# print(format(x, 'b'))
# x = int(input(), 2)
# print(format(x, 'o'))


# n = str(input())
# n = n.upper()
# a = {}
# for i in n:
#     if i in a:
#         a[i] += 1
#     else:
#         a[i] = 1
# r = []
# for key, value in a.items():
#     if value == max(a.values()):
#         r.append(key)
# if len(r) >= 2:
#     print('?')
# else:
#     print(r[0])

# x = list(map(str, input().split()))
# print(x)
# print(len(x))

# case = int(input())
# a = []
# for _ in range(case):
#     a.append(list(map(int, input().split())))
# dp = [0,0,0]
#
# for i in range(case):
#     dp[0], dp[1], dp[2] = min(dp[1], dp[2])+a[i][0], min(dp[0],dp[2])+a[i][1], min(dp[0],dp[1])+a[i][2]
# print(min(dp))

# N = int(input())
# dp = [0,2,3]
# for i in range(3,N+1):
#     if i%4==0:
#         dp.append(dp[i//2]*2)
#     elif i%2!=0:
#         dp.append(dp[i//2]+dp[i//2+1])
#     else:
#         dp.append(dp[i-1]+1)
#
# print(dp[N])


# n = int(input())
# dp = [0 for i in range(31)]
# dp[2] = 3
# for i in range(4, 31, 2):
#     dp[i] = dp[2] * dp[i - 2]
#     for j in range(4, i, 2):
#         dp[i] += 2 * dp[i - j]
#     dp[i] += 2
# print(dp[n])


# case = int(input())
# for _ in range(case):
#     n, m = map(int, input().split())
#     if n==m:
#         print(1)
#     else:
#         a = 1
#         b = 1
#         c = 1
#         for i in range(2, m+1):
#             a *= i
#         for i in range(2, n+1):
#             b *= i
#         for i in range(2, (m-n)+1):
#             c *= i
#         print(a // (b*c))


# n = int(input())
# dp = [0,1,1]
# for i in range(3,n+1):
#     dp.append(dp[i-1]+dp[i-2])
# print(dp[-1])


# n, k = map(int, input().split())
# a = []
# for _ in range(n):
#     a.append(int(input()))
# dp = [0 for _ in range(k+1)]
# dp[0]=1
# for i in a:
#     for j in range(i,k+1):
#         if j>=i:
#             dp[j] += dp[j-i]
# print(dp[k])


# n, k = map(int, input().split())
# a = []
# dp = [0 for _ in range(k+1)]
#
# for _ in range(n):
#     x = int(input())
#     if x<=k:
#         a.append(x)
# a.sort()
# for i in a:
#     for j in range(i,k+1):
#         if j%i == 0:
#             dp[j] = dp[j-i] + 1
#         if dp[j-i]!=0 and dp[j]==0:
#             dp[j] = dp[i] + dp[j-i]
#         elif dp[j-i]!=0 and dp[j]!=0:
#             dp[j] = min(dp[i] + dp[j-i] , dp[j])
# if dp[-1] ==0:
#     print(-1)
# else:
#     print(dp[-1])


# x, y, w, h = map(int, input().split())
# print(min(x, w-x, y, h-y))


# def find(x):
#     if p[x]==x: #어떤 원소 a 가 주어질 때, 이 원소가 속한 집합을 반환합니다.
#         return x
#     else:
#         y = find(p[x])
#         p[x] = y
#         return y
#
# def union(x,y): #두 정점을 연결하는 거임.
#     x = find(x) #x가 속한 집합은?
#     y = find(y) #y가 속한 집합은?
#                                         # if x!=y:
#                                         #     p[y] = x #연결했다==같은 집합 소속이다. 근데 x,y가 속해있는 집합이 서로 다르면 안되니까 같게 해주는거임.
#     if x!=y: #짧은 트리의 루트가 긴 트리의 루트를 가리키게 하는 것이 좋음.
#         if rank[x] > rank[y]:
#             p[y]=x
#         else:
#             p[x]=y
#
#             if rank[x]==rank[y]:
#                 rank[y]+=1
#
#
# v, e = map(int, input().split()) #V가 정점, E가 간선
# graph = []
# rank = [0 for _ in range(v+1)]
# p = [i for i in range(v+1)] #정점 수만큼의 리스트
#
# for _ in range(e):
#     a, b, c = map(int, input().split())
#     graph.append([c,a,b])
#
# graph.sort(key=lambda x:x[0]) #첫 인자(가중치) 기준 정렬
# e_count = 0
# mst = 0 #가중치 저장소
# for i in range(e):
#     dis = graph[i][0] #가중치
#     start = graph[i][1] #간선 시작점
#     end = graph[i][2] #간선 끝점 즉, start와end는 이어져있는 정점임.
#     if find(start) != find(end): #이어져있으면 find 각각 값이 같아야하니까
#         union(start, end) #이렇게 이어주기.
#         mst += dis
#         e_count += 1
#     if e_count==v-1: #모든 정점이 연결됐다면 스탑.
#         break
# print(mst)




# from collections import deque
#
# v, e, s = map(int, input().split())
# a = [[0 for _ in range(v+1)] for _ in range(v+1)]
#
# for _ in range(e):
#     x, y = map(int, input().split())
#     a[x][y], a[y][x] = 1,1
#
# def dfs(a, s, result):
#     result += [s]
#     for i in range(1, v+1):
#         if a[s][i] and i not in result:
#             result = dfs(a, i, result)
#     return result
#
# print(*dfs(a, s, []))
#
# def bfs(s):
#     queue = deque([s])
#     result = [s]
#     while queue:
#         s = queue.popleft()
#         for i in range(1, v+1):
#             if a[s][i] and i not in result:
#                 result += [i]
#                 queue.append(i)
#     return result
# print(*bfs(s))


# nums = [2, 7, 11, 15]
# target = 9
# nums_map = {}
# for i , num in enumerate(nums):
#     print(i)
#     nums_map[num]=i
# print(nums_map)

# nums = [-2,-1,1,3,-1,0,2]
# ans = []
# nums.sort()

# for i in range(len(nums)-2):
#     if i>0 and nums[i]==nums[i-1]:
#         continue
#     l, r = i+1, len(nums) - 1

#     while l<r:
#         sum = nums[i] + nums[l] + nums[r]
#         if sum<0:
#             l += 1
#         elif sum>0:
#             r -= 1
#         else:
#             ans.append([nums[i], nums[l], nums[r]])
#             while l<r and nums[l]==nums[l+1]:
#                 l+=1
#             while l<r and nums[r]==nums[r-1]:
#                 r-=1
#             l+=1
#             r-=1
# print(ans)




# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# graph = collections.defaultdict(list)
# history = []
# for a, b in sorted(tickets, reverse = True):
#     graph[a].append(b) #출발지별 도착지묶음
# queue = []
# def dfs(a):
#     while graph[a]:
#         x = graph[a].pop()
#         dfs(x)
#     history.append(a)
# dfs("JFK")
# print(history[::-1])



# a = collections.defaultdict(list)
# times = [[2,1,1],[2,3,1],[3,4,1]]
# for u, v, w in times:
#     a[u].append((v,w))
# print(a)

# time, node = heapq.heappop()


# class TrieNode:
#     def __init__(self):
#         self.word = False
#         self.children = collections.defaultdict(TrieNode)

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         node = self.root
#         for char in word:
#             node = node.children[char]
#         node.word = True

#     def search(self,word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return node.word  #마지막에 word가 True인지 확인하면 되는 것임.

#     def startsWith(self, prefix):
#         node = self.root
#         for char in prefix:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return True


# record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# for i in range(len(record)):
#     record[i] = record[i].split()
# print(record)
from collections import defaultdict
# def multiply(arr):
#     ans = 1
#     for n in arr:
#         ans *= n
#     return ans
# d = defaultdict(list)
# clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
# for i in range(len(clothes)):
#     d[clothes[i][1]] += [clothes[i][0]]
# lengths = [len(v) for v in d.values()]
# print(multiply(lengths)+sum(lengths))




# n = 40
# li = [1]
# lengths = round(pow(n , 1/3))
# for i in range(1, lengths+1):
#     li.append(li[i-1] + pow(3,i))

# n = 20
# answer_list = ["4","1","2"]
# answer = ''
# while n > 0:
#     answer = answer_list[n%3] + answer
#     if not n%3:
#         n = n//3 - 1
#     else:
#         n //= 3
# print(answer) 
# priorities = [1,1,9,1,1,1]
# location = 0

# queue = [(i,p) for i,p in enumerate(priorities)]
# print(queue)
# cur = queue.pop(0)
# print(cur)
# print(cur[1])
# any(cur[1] < q[1])

# def solution(priorities, location):
#     answer = 0
#     priorities_copy = [0 for _ in range(len(priorities))]
#     priorities_copy[location] = 1 
#     while True:
#         if priorities[0] == max(priorities):
#             answer += 1
#             if priorities_copy[0]==1:
#                 break
#             else:    
#             # if not priorities_copy[0]:
#                 del priorities[0] 
#                 del priorities_copy[0]
#         else:
#             priorities.append(priorities[0])
#             del priorities[0]
#             priorities_copy.append(priorities_copy[0])
#             del priorities_copy[0]
#     return answer
# print(solution(priorities, location))


# x = "1195"
# y = "119"
# z = "19"
# p = ["1195","119","19","114"]
# p = sorted(p, key=len)
# print(p)

# print(p[3][:3])
# if z in x:
#     print(False)
# else: print(True)


# for j in range(i+1, len(phone_book)):
#             if len(phone_book[i]) >= len(phone_book[j]):
#                     long, short =  phone_book[i], phone_book[j]
#             else: short, long =  phone_book[i], phone_book[j]

#             if short in long:
#                 return False



import heapq
# def solution(scoville, K):
#     # l = len(scoville)
#     answer = 0
#     heapq.heapify(scoville)
#     # if scoville[0] >= K:
#     #     return 0
#     while len(scoville) > 1:
#         answer += 1
#         new = heapq.heappop(scoville) + 2* heapq.heappop(scoville)
#         if new >= K:
#             break
#         else:
#             heapq.heappush(scoville, new)
#     if answer==l-1:
#         return -1
#     else:return answer

# name = 'ABCBAAAAAB'
name = "BABAAAAAB"
# cnt = [min(26 - ord(i) + 65, ord(i) - 65) for i in name if i != 'A']

# print(name[:2])
# print(ord('A')-ord('B'))
# idx = [i for i, v in enumerate(name) if v!='A']
# print(idx)
# graph = [idx[i+1]-idx[i] for i in range(len(idx)-1)] + [len(name) - idx[-1]]
# print(graph)
# if name[0] == 'A':
#     idx = [0] + idx
#     graph = [idx[1]] + graph
# print(idx, graph)
# answer = [2 * sum(graph[:i]) + (len(name) - idx[i + 1]) for i, v in enumerate(idx) if 0 < v < len(name) // 2] + [idx[-1], len(name) - idx[1]]
# print(cnt)
# print(sum(cnt))
# print(answer)



# make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
# idx, answer = 0, 0
# while True:
#     answer += make_name[idx]
#     make_name[idx] = 0
#     if sum(make_name) ==0:
#         break
#     left, right = 1, 1
#     while make_name[idx - left] ==0:
#         left +=1
#     while make_name[idx + right] ==0:
#         right +=1
#     answer += left if left < right else right
#     idx += -left if left < right else right

# print(answer)
import collections


# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]


# import collections
# a = ['apple', 'banana', 'cherry']
# print(collections.Counter(a))

# d = defaultdict(int)
# for i in a:
#     d[i] += 1
# print(d)

# d = {'apple':2, 'banana':4, 'cherry':6}
# print(collections.Counter(d))

# f = collections.Counter(apple=1, banana=3, cherry=5)
# print(f)

# string_count = 'Hello World! hHeElL'
# counter = collections.Counter(string_count)
# print(counter)

# for u,v in counter.items():
#     print(u,":",v)

# d=list(d)
# d_d = ["banana","cherry"]
# answer = collections.Counter(d) - collections.Counter(d_d)
# print(answer)
# print(list(answer.keys()))


# s = collections.Counter('sbs')
# k = collections.Counter('kbs')
# print(s&k)
# m = s|k
# m.update("mbc")
# print(m)



# genres = ["classic", "pop","classic", "classic", "pop","kpop","rock","rock"]
# plays = [500, 600, 150, 800, 2500,1700,500,500]
# genres_rank = []
# answer = []
# info = defaultdict(list)
# d = defaultdict(int)
# for i, j in enumerate(genres):
#     d[j] += plays[i]
#     info[j] += [(i, plays[i])]
# # dd = sorted(d.items(), reverse=True, key=lambda item:item[1])
# for key, value in sorted(d.items(), reverse=True, key=lambda item:item[1]):
#     genres_rank.append(key)

# print(genres_rank)
# print(info)
# for genre in genres_rank:
#     info[genre].sort(reverse=True, key=lambda x: x[1])

# print(info)
# for genre in genres_rank:
#     for i in range(min(len(info[genre]) , 2)):
#         answer.append(info[genre][i][0])
# print(answer)



# pi = {'a':3,'b':1,'c':4,'aa':1,'bb':5,'cc':9}
# pi_list = []
# for key, value in sorted(pi.items(), key=lambda x:-x[1]):
#     pi_list.append(key+":"+str(value))
# print(pi_list)


# jobs = [[2,5],[0, 3],[0,1], [4,4], [1, 9], [2, 6],[10,5]]
# t = 0
# jobs.sort()
# flow = []
# print(jobs)
# for start, cost in jobs:
#     while start >= t:
#         t += cost
#         heapq.heappush(flow, [cost, start])
#         if  
#         cost, start = heapq.heappop(flow)
#     else:
#         heapq.heappush(flow, [cost, start])


# jobs_tuplelist = []
# answer = 0
# time = 0 
# for i in jobs:
#     jobs_tuplelist.append((i[1],i[0]))
# # heapq.heapify(jobs)
# # print(heapq.heappop(jobs))
# # print(heapq.heappop(jobs))w
# # print(heapq.heappop(jobs))
# heapq.heapify(jobs_tuplelist)
# while jobs_tuplelist:
#     temp = heapq.heappop(jobs_tuplelist)
#     answer += (time-temp[1]) + temp[0]
#     time += temp[0]
# print(answer // len(jobs))


# number = "4177252841"
# k = 4
# stack = [number[0]]
# for num in number[1:]:
#     while stack and stack[-1]<num and k:
#         k-=1
#         stack.pop()
#     stack.append(num)
# if k:
#     stack = stack[:-k]
# print(stack)
# print(''.join(stack))



# n = 18
# answer = 0
# li = []
# for i in range(n):
#     li.append(i+1)
# print(li)
# for i in range(n//2+1):
#     for j in range(i+1,n//2+1):
#         if li[i]+li[j]==n:
#             answer += 1
#         elif li[i]+li[j] > n:
#             break
#         li[i] += li[j]
# print(answer+1)

# import collections

# n = 15
# n2 = bin(n)[2:]
# counter = collections.Counter(n2)
# while True:
#     n += 1
#     nn2 = bin(n)[2:]
#     counter2 = collections.Counter(nn2)
#     if counter['1']==counter2['1']:
#         print(n)
#         break

from collections import deque

people = [70,50,80,50,  15,25,90]
limit = 100
answer = 0 

people.sort(reverse=True)
print(people)

q = deque(people)

while q:
    plus = 0
    temp = q.popleft()
    if q and q[-1] <= limit-temp:
        temp += q.pop()
    answer += 1
print(answer)


























#memo