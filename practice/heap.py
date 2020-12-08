# class MaxHeap:
#
#     def __init__(self):
#         self.data = [None]
#
#     def maxHeapify(self, i):
#         left = 2*i
#         right = (2*i) + 1
#         smallest = i
#
#         if left < len(self.data) and self.data[i] < self.data[left]:
#             #왼쪽이 존재하는지, 그리고 왼쪽 값이 ___보다 더 큰지?
#             smallest = left
#         if right < len(self.data) and self.data[i] < self.data[right]:
#             smallest = right
#         if smallest != i:
#             self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
#             self.maxHeapify(smallest)
#
#     def insert(self, item):
#         self.data.append(item) #append하면 제일 아래노드에 집어넣게 됨.
#         i = len(self.data) - 1 #방금 넣은 자리임.
#
#         while i > 1:
#             if self.data[i] > self.data[(i//2)]: #부모 노드보다 값이 크면 둘이 값을 바꿔줌
#                 self.data[i], self.data[(i//2)] =  self.data[(i//2)], self.data[i]
#                 i = i // 2
#             else: break
#
#     def remove(self):
#         if len(self.data) > 1:
#             self.data[1], self.data[-1] = self.data[-1], self.data[1]
#             data = self.data.pop(-1)
#             self.maxHeapify(1)
#         else:
#             data = None
#         return data


#============================================================#

class minHeap:
    def __init__(self):
        self.queue = [None]

    def swap(self, x, y):
        self.queue[x], self.queue[y] = self.queue[y], self.queue[x]

    def insert(self, n):
        self.queue.append(n)
        i = len(self.queue) - 1
        while i>1: #root로 올 때가지 부모와 비교하며 더 작으면 교체
            parent = i // 2
            if self.queue[i] < self.queue[parent]:
                self.swap(i, parent)
                i = parent
            else: break

    def delete(self):
        if len(self.queue) > 1:
            self.swap(1, len(self.queue)-1) #마지막 원소와 root를 바꿔주고
            ans = self.queue.pop(len(self.queue)-1) #마지막 원소 제거 (즉 처음의 root를 제거)
            self.minHeapify(1) #root에서부터 heapiffy를 시작
        else: ans = 0
        return ans

    def leftchild(self, i):
        return i*2
    def rightchild(self, i):
        return i*2 + 1

    def minHeapify(self, i): #자식들과 자신을 비교하면서 내려가는 함수.
        left = self.leftchild(i)
        right = self.rightchild(i)
        smallest = i #일단 작은 걸 자신으로 놓고

        if left <= len(self.queue)-1 and self.queue[left] < self.queue[smallest]:
            smallest = left
        if right <= len(self.queue)-1 and self.queue[left] < self.queue[smallest]:
            smallest = right
        if smallest != i:
            self.swap(i, smallest)
            self.minHeapify(smallest)

if __name__ == '__main__':
    case = int(input())
    h = minHeap()
    for _ in range(case):
        x = int(input())
        if x == 0:
            print(h.delete())
        else:
            h.insert(x)






















#d
