import sys
result = []
n = int(sys.stdin.readline())

for i in range(n):
    cmd = str(sys.stdin.readline())
    f = int(sys.stdin.readline())
    if "RR" in cmd :
        cmd = cmd.replace("RR", "")
    a = eval(input())

    for i in range(len(cmd)):
        if cmd[i] == "R" :
            a.reverse()
        elif cmd[i] == "D" :
            if len(a) < 1:
                a = "error"
                break
            else: 
                del a[0]
    result.append(a)
print(*result, sep='\n')