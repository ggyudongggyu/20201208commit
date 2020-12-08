time = int(input())
for i in range(time):
    n, str = input().split()
    result = ''
    for k in str:
        result = result + int(n)*k
    print(result)
