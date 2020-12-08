import sys
time_table = []
for i in range(int(input())):
    time_table.append(list(map(int, input().split())))

time_table.sort(key=lambda x:(x[1], x[0]))
cnt = end_time = 0
for i in time_table:
    if end_time <= i[0]:
        end_time = i[1]
        cnt += 1
print(cnt)

# cnt = 1
# end_time = time_table[i][1]
#로하면 왜 안되는거지 
