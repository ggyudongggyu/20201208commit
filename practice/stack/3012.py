def check(txt):
    table = {   ')' : '('}
    stack = []
    for char in txt:
        if char not in table:
            stack.append(char)
        elif table[char] != stack.pop():
            return False

case = int(input())
for i in range(case):
    txt = str(input())
    if check(txt) :
        print("YES")
    else: print("NO")
    


