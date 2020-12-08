a,b = input().split()
a2 = ''.join(reversed(a))
b2 = ''.join(reversed(b))
if a2>b2:
    print(a2)
else:
    print(b2)

# a2=[]
# b2=[]
#
#
# # for i in range(len(a)-1):
# #     a2[(len(a)-1-i)] = a[i]
# # for i in range(len(b)-1):
# #     b2[(len(b)-1-i)] = b[i]
# print(a)
# print(a2)
# print(b2)

#
# for i in range(len(a)-1):
#     a2 = a2 + a[(len(a))]
