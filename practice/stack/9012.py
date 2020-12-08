for _ in range(int(input())):
    vps = list(input())
    while len(vps) != 0:
        if vps[0] == ')':
            print('NO')
            break
        else:
            if ')' in vps:
                vps.remove('(')
                vps.remove(')')       # 괄호 쌍 제거
            else:                       # 괄호 쌍X: NO
                print('NO')
                break

    if len(vps) == 0:
        print('YES')
