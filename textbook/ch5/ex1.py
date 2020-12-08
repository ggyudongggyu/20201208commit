# from collections import deque
# def isPallindrome(s: str) -> bool:
#     strs = deque([])

#     for char in s:
#         if char.isalnum():
#             strs.append(char.lower())
#     while len(strs) > 1:
#         if strs.popleft() != strs.pop():
#             return False
#     return True

# X = str(input())
# print(isPallindrome(X))

# ================================= #

import re

def isPallindrome(s: str):
    s = s.lower()
    s = re.sub('[^a-z0-9]','',s)

    return s == s[::-1]
X = str(input())
print(isPallindrome(X))