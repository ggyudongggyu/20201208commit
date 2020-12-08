max = 0
for i in range (9):
    x = int(input())
    if x>max:
        max=x
        flag=i+1
print(max)
print(flag)
