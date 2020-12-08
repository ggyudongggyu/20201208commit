import sys
N = int(sys.stdin.readline())
cnt = 0
A = list(map(int, input().split()))
B, C = map(int, input().split())
for i in range(N):
    A[i] -= B
    if A[i] > C:
        if A[i]%C == 0:
            cnt += A[i]//C
        else: cnt += A[i]//C + 1
        print("첫if돌입")
    elif A[i] > 0 :
        cnt += 1
        print("둘째if돌입")
    cnt += 1
    print(i,"번끝나고의 cnt = ",cnt)
print(cnt)
