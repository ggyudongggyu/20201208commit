# import sys
# N = int(input())
#
# dic = {}
#
# for i in range(N):
#     a = int(sys.stdin.readline())
#     if a in dic:
#         dic[a] =  dic[a] +1
#     else:
#         dic[a] = 1
#
# for sorted in sorted(dic.items()):
#     for i in range(sorted[1]):
#         print(sorted[0])

# ==
# sorted_dict = sorted(my_dict.items())
# for i in range(len(sorted_dict)):
#     for j in range(sorted_dict[i][1]):
#         print(sorted_dict[i][0])

# 10001 리스트 사용하는 방법
import sys
N = int(input())
check_list = [0] * 10001

for i in range(N):
    input_num = int(sys.stdin.readline())
    check_list[input_num] = check_list[input_num] + 1
for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]): # i의 수만큼 (중복되어도 여러번 나오게끔)
            print(i)
