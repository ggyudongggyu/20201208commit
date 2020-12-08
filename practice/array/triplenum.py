a=int(input())
b=int(input())
c=int(input())
d_mun=list(str(a*b*c))
for i in range (10):
    d_count=d_mun.count(str(i))
    print(d_count)
