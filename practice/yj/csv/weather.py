import csv
from matplotlib.pyplot import *
from pylint import graph
import matplotlib.pyplot as plt

max_temp = -99
min_temp = 100
max_date = ""
min_date = ""
f = open('SURFACE_ASOS_108_DAY_2018_2018_2019.csv', 'r')
data = csv.reader(f, delimiter=',')  #리스트로 읽음
header = next(data) #각 항목이 뭘 나타내는지
max_temp_list=[]
max_date_list=[]
min_date_list=[]
min_temp_list=[]
month = '01'

for x in data:
    if x[1].split('-')[1] != month:
        max_temp_list.append(max_temp)
        min_temp_list.append(min_temp)
        max_date_list.append(max_date)
        min_date_list.append(min_date)
        max_temp = -99
        min_temp = 100
        month = x[1].split('-')[1]
    if x[5]=='' or x[3]=='':
        continue
    high_temp = float(x[5])
    low_temp = float(x[3])
    if high_temp>max_temp:
        max_temp = high_temp
        max_date = x[1]
    if low_temp < min_temp:
        min_temp = low_temp
        min_date = x[1]
max_temp_list.append(max_temp)
max_date_list.append(max_date)
min_date_list.append(min_date)
min_temp_list.append(min_temp)

f.close()
print(max_temp_list)
print(max_date_list)
print(min_temp_list)
print(min_date_list)

month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

title('plot Graph')
plot(month_list, max_temp_list, label = 'Max_temp',  marker = '*')
plot(month_list, min_temp_list, label = 'Min_temp', marker = '^')
legend()
show()


# plt.title('plot Graph')
# plt.plot(month_list, max_temp_list)
# plt.plot(month_list, min_temp_list)
# plt.ylim(-20,40)
# plt.show()

