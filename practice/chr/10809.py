abc = "abcdefghijklmnopqrstuvwxyz"
str = input()
a=[]
b=[]
for i in str:
    a.append(i)

for j in abc:
    for k in range(len(a)):
        if j == a[k]:
            b.append(k)
            break
        elif k < len(a)-1:
            continue
        else:
            b.append(-1)
print(*b)
