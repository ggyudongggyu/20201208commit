zero = [1, 0, 1]
one = [0, 1, 1]
def d(n):
    if len(zero) <= n:
        for i in range(len(zero) , n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print("%d %d"%(zero[n],one[n]))

for n in range(int(input())):
    d(int(input()))
