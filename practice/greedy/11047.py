N, K = map(int, input().split())
l = []
cnt = 0
sum = K
for i in range(N):
    a = int(input())
    if a <= K :
        l.append(a)

# for i in range(len(l)):
#     cnt = cnt + K//l[-1]
#     sum = K - l[-1]*cnt
#     l.pop()
#     if l[-1] > sum:
#         l.pop()

for i in l:
    cnt += K // -i
    K = K % -i
print(cnt)
