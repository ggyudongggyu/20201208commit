s = str(input())

if len(s)<2 or s==s[::-1]:
    print(len(s))
else:
    for i in range(len(s),0,-1):
        if s[i:len(s)]==s[len(s)-1:i-1:-1]:
            p = s[len(s)-1:i-1:-1]
    print(2 * len(s) - len(p))
# s='zabcba'
# print(s[4:6])
# print(s[5:3:-1])