n = input()
t = 0
for i in n:
    if ord(i) > ord("V"):
        t = t + 9
    elif ord(i) > ord("S"):
        t = t + 8
    elif ord(i) > ord("O"):
        t=t+7
    elif ord(i) > ord("L"):
        t=t+6
    elif ord(i) > ord("I"):
        t=t+5
    elif ord(i) > ord("F"):
        t=t+4
    elif ord(i) > ord("C"):
        t=t+3
    else:
        t=t+2
t = t + len(n)

print(t)


# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# a = input()
# ret = 0
# for j in range(len(a)):
#     for i in dial:
#         if a[j] in i:
#             ret += dial.index(i)+3
# print(ret)
