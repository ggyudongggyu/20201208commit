a= []
n = int(input())
if n ==1: print(1)
else:
    for i in range(1,n+1):
        a.append(i)
    while True:
        del a[0]
        if len(a)==1:
            break
        a.append(a[0])
        del a[0]
        if len(a)==1:
            break
    print(a[0])

#
# a = [4,3,2]
# a.append(a[0])
# del a[0]
# print(a)
