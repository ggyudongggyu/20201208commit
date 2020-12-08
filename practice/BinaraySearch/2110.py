#집 개수 _ 공유기 대수
#집 좌표
#집 좌표 ...
import sys
H , C = map(int, sys.stdin.readline().split())
A = []
for _ in range(H):
    A.append(int(sys.stdin.readline()))
i, f = min(A), max(A)
m = (i+f)//2

