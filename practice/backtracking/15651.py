N, M = map(int, input().split())
out = []  # 출력 내용

def solve(depth, N, M):
    if depth == M:  # 탈출 조건
        print(' '.join(map(str, out)))  # list를 str으로 합쳐 출력
        return
    for i in range(N):  # 탐사 check 하면서
            out.append(i+1)  # 탐사 내용
            solve(depth+1, N, M)  # 깊이 우선 탐색
            out.pop()  # 탐사 내용 제거

solve(0, N, M)
