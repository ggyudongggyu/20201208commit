import operator
str = list(input())
str2 = [w.upper() for w in str]
abc = []
for i in range(26):
    abc.append(chr(65+i))
cnt = 0
d = {}
for a in str2:
    if a in d:
        d[a] = d[a] + 1
    else:
        d[a] = 1

for i in d.keys():
    if d[i] == max(d.values()):
        cnt = cnt + 1

if cnt>1 :
    print("?")
else:
    print(max(d.items(), key=operator.itemgetter(1))[0])

# for i in abc:
#     for k in str2:
#         if d[key]==max(d.values())
#
#
# for i in abc:
#     if
#         print("?")
#     else:
#         print(max(d.items(), key=operator.itemgetter(1))[0])
# print(abc)
# print(str2)
# print(d)
# print(max(d.values()))
