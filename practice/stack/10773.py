
stack = []
for i in range(int(input())):
    X = int(input())
    if X == 0:
        stack.pop()
    else: stack.append(X)
if bool(stack) is False:
    print(0)
else:print(sum(stack))
