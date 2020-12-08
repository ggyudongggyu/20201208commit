import sys
from collections import deque

class dq():
    def __init__(self):
        self.deque = deque([])
    def push_front(self, num):
        self.deque.appendleft(num)
    def push_back(self, num):
        self.deque.append(num)
    def pop_front(self):
        if len(self.deque)==0:
            print(-1)
        else:
            print(self.deque.popleft())
    def pop_back(self):
        if len(self.deque)==0:
            print(-1)
        else:
            print(self.deque.pop())
    def size(self):
        print(len(self.deque))
    def empty(self):
        if len(self.deque)==0:
            print(1)
        else: print(0)
    def front(self):
        if len(self.deque)==0:
            print(-1)
        else:
            print(self.deque[0])
    def back(self):
        if len(self.deque)==0:
            print(-1)
        else: print(self.deque[-1])

n = int(input())
s = dq()
for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push_front":
        s.push_front(command[1])
    elif command[0] == "push_back":
        s.push_back(command[1])
    elif command[0] == "pop_front":
        s.pop_front()
    elif command[0] == "pop_back":
        s.pop_back()
    elif command[0] == "size":
        s.size()
    elif command[0] == "empty":
        s.empty()
    elif command[0] == "back":
        s.back()
    elif command[0] == "front":
        s.front()