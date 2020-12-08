import csv
import random

namelist = ['park', 'komori', 'sonehara','nobusawa','li','shimizu']
# test = []
v = open('C:\\Users\\i3_OWNER\'s\\Documents\\pytest\\Weekly_Gift.csv')
r = csv.reader(v)
row0 = next(r)
for i in random.sample(namelist, 3):
    row0.append(i)
print(row0)

# for i in range(3):
    # B = random.randrange(0, len(namelist)-1)
# B = random.sample(namelist, 3)
#     # if B in test:
# row0.append(namelist[B])
# print(row0)
