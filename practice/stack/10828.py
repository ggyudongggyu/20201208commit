
# def pop(stock):
#     if bool(stock) is True:
#         print(stock.pop())
#     else:print(-1)
#
# def size(stock):print(len(stock))
#
# def empty(stock):
#     if bool(stock) is True:print(0)
#     else:print(1)
#
# def top(stock):
#     if bool(stock) is False:print(-1)
#     else:print(stock[-1])



import sys
stock = []
times = int(input())
for i in range(times):
    __input = sys.stdin.readline()
    c = __input.split()[0]
    if c == "push" :
        stock.append(int(__input.split()[1]))
    elif c == "pop":
        if bool(stock) is True:
            print(stock[-1])
            stock.pop()
        else:
            print('-1')
    elif c == "size":
        print(len(stock))
    elif c == "empty":
        if bool(stock) is True:
            print(0)
        else:
            print(1)
    elif c == "top":
        if bool(stock) is False:
            print('-1')
        else:
            print(stock[-1])
