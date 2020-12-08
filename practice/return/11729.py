# N개의 하노이탑을 END타워로 옮기기 위해서는
# N-1 개의 하노이탑을 MID타워로 옮겨야 함.

def hanoi(plate, start, mid, end):
    if plate == 1:
        print(start, end)
    else:
        hanoi(plate-1, start, end, mid)
        print(start, end)
        hanoi(plate-1, mid, start, end)

N = int(input())
print(2**N - 1)
hanoi(N, 1, 2, 3)
