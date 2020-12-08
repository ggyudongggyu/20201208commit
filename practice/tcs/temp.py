import sys
print("本日の気温を入力してください：", end="")
C = float(input())
F = C*9/5 + 32
print("華氏: {0:.1f}".format(F))
