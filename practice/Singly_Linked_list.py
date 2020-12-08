class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class singly_linked_list:
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node
    
    def find_data(self, num):
        temp = self.head
        #temp는 None이거나 node 둘 중 하나. temp.data와 temp.next 사용 가능
        idx = 0
        while temp:
            if temp.data!=num:
                idx += 1
                temp = temp.next
            else:
                return idx
        return -1 #if cannot find, return -1
    
    def show_all(self):
        temp = self.head
        printout = ""
        while temp:
            printout += str(temp.data)
            if temp.next:
                printout += "->"
            temp = temp.next
        return printout

    def delete_with_index(self, idx):
        temp = self.head
        i = 0 
        prev_node = None
        next_node = self.head.next
        if idx==0:
            self.head = next_node
        else:
            while i < idx:
                if temp.next:
                    prev_node = temp
                    temp = next_node
                    next_node = next_node.next
                else:
                    break
                i += 1
            if i==idx:
                prev_node.next = next_node
            else: print(-1)

    def insert_with_index(self, idx, node):
        temp = self.head
        i = 0 
        prev_node = None
        if idx==0:
            if self.head:
                # next_node = self.head
                # node.next = next_node
                # return node
                # 원리상으론 삽입이 가능하나, node에 붙이기만 했지 원래 self객체에 반환이 안되는거라 아래로 구현.

                next_node = self.head
                self.head = node
                self.head.next = next_node
            else: 
                self.head = node
        else:
            while i < idx:
                if temp:
                    prev_node = temp
                    temp = temp.next
                else: break
                i += 1
            if i==idx:
                prev_node.next = node
                node.next = temp
            else: print(-1)
        

s = singly_linked_list()
s.append(Node(3))
s.append(Node(2))
s.append(Node(1))
s.append(Node(4))
print(s.show_all())
print(s.find_data(1))
s.delete_with_index(2)
s.insert_with_index(2, Node(5))
s.insert_with_index(8, Node(5))
print(s.show_all())
