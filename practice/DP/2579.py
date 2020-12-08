p = []
len = int(input())
for i in range(len):
    p.append(int(input()))

p[1] = p[1] + p[0]
p[2] = p[2] + p[0]
for i in range(3, len-2):
    p[i] = p[i] + max(p[i-1], p[i-2])
p[-2] = p[-2] + p[-4]
p[-1] = p[-1] + max(p[-2], p[-3])
print(p)
print(p[-1])
