n=int(input())
p=[0,0,1,1]
if n < 4:
    print(p[n])
else:
    for i in range(4,n+1):
    # print("i=", i)
        # if i == 1:
        #     p.append(0)
        if i % 3 == 0 and i % 2 == 0:
            p.append(min(p[i//2]+1, p[i//3]+1, p[i-1]+1))
        elif i % 3 == 0 and i % 2 != 0:
            p.append(min(p[i//3]+1, p[i-1]+1))
        elif i % 2 == 0 and i % 3 != 0 :
            p.append(min(p[i//2]+1, p[i-1]+1))
        else:
            p.append(p[i-1]+1)
# print(p)
    print(p[-1])
