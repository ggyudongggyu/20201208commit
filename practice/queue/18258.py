n = int(input())
q = []

for i in range(n):
    cmd=[]
    cmd.append(input().split())
    if cmd[0][0] == "push":
        q.append(int(cmd[0][-1]))
    elif cmd[0][0] == "front":
        if len(q) == 0:
            print(-1)
        else: print(q[0])
    elif cmd[0][0] == "back":
        if len(q) == 0:
            print(-1)
        print(q[-1])
    elif cmd[0][0] == "pop":
        if len(q) > 0:
            print(q[0])
            q = q[1:]
        else: print(-1)
    elif cmd[0][0] == "size":
        print(len(q))
    elif cmd[0][0] == "empty":
        if len(q)==0: print(1)
        else:print(0)


# n = int(input())
# q = []
# for i in range(n):
#     cmd = str(input())
#     if "push" in cmd:
#         q.append(int(cmd[-1]))
#     elif "front" in cmd:
#         print(q[0])
#     elif "back" in cmd:
#         print(q[-1])
#     elif "pop" in cmd:
#         if len(q) > 0:
#             print(q[0])
#             q = q[1:]
#         else: print(-1)
#     elif "size" in cmd:
#         print(len(q))
#     elif "empty" in cmd:
#         if len(q)==0: print(1)
#         else:print(0)
