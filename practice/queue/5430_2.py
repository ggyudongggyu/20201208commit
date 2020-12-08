import sys
result = []
n = int(sys.stdin.readline())
for i in range(n):
    R = 0   
    cmd = str(sys.stdin.readline())
    f = int(sys.stdin.readline())
    if "RR" in cmd :
        cmd = cmd.replace("RR", "")
    a = eval(input())
    
    for i in range(len(cmd)):
        if cmd[i] == "R" :
            R += 1
        elif cmd[i] == "D" :
            if len(a) < 1:
                a = "error"
                break
            else: 
                if R%2 == 0 :
                    del a[0]
                else :
                    del a[-1]
    if a=="error" :
        result.append(a)
    elif R%2 != 0 :
        a.reverse()
        result.append(a)
    else: result.append(a)
    
print(*result, sep='\n')