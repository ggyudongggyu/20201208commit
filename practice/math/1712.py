# A = 고정비용 : 몇대 생산하든 고정으로
# B = 가변비용 : 한대당 가격
# C = 판매가

A, B, C = map(int, input().split())

if C-B <= 0:
    print("-1")
else:
    print(int(A/(C-B)+1))
