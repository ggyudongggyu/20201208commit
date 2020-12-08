node = int(input())
node_dict = {}
for _ in range(node):
    a, b, c = map(str, input().split())
    node_dict[a]=(b,c)

def first(tree):
    temp = ['A']
    ans = ''

    while temp:
        now = temp.pop()
        ans += now

        if tree[now][1] != '.':
            temp.append(tree[now][1])
        if tree[now][0] != '.':
            temp.append(tree[now][0])

    print(ans)

first(node_dict)

def second(tree):
    temp = ['A']
    ans= ''

    while temp:
        if tree[temp[-1]][0] != '.' and tree[temp[-1]][0] not in ans:
            temp.append(tree[temp[-1]][0])
        elif tree[temp[-1]][1] in ans:
            temp.append(tree[temp[-1]][1])
        else:
            now = temp.pop()
            ans += now
            if tree[now][1] != '.':
                temp.append(tree[now][1])
    print(ans)

second(node_dict)

def third(tree):
    temp = ['A']
    ans= ''

    while temp:
        if tree[temp[-1]][0] != '.' and tree[temp[-1]][0] not in ans:
            temp.append(tree[temp[-1]][0])
        elif tree[temp[-1]][1] == '.' or tree[temp[-1]][1] in ans:
            ans += temp.pop()          
        else:
            temp.append(tree[temp[-1]][1])
            
    print(ans)
third(node_dict)
            