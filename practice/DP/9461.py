__list__ = [0]*101
__list__[0]=0
__list__[1]=__list__[2]=__list__[3]=1
__list__[4]=__list__[5]=2

# def pado(n, __list__):
#     if n<6:
#         return(__list__[n])
#     else:
#         __list__[n] = pado(n-5, __list__)+pado(n-1, __list__)
#         return(__list__[n])

case = int(input())
for i in range(case):
    n=int(input())
    for j in range(5,n+1):
        __list__[j] = __list__[j-1] + __list__[j-5]
    print(__list__[n])
