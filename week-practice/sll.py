class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    def insert_begin(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node
        return
    def insert_end(self, data):
        node = Node(data)
        if self.head is None:
            self.insert_begin(data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        return
    def count(self):
        count = 0
        temp = self.head
        while temp:
            temp = temp.next
            count += 1
        return count
    def insert_index(self, index, data):
        if index < 0 or index > self.count():
            print("invalid index")
            return
        if index == 0:
            self.insert_begin()
            return
        temp = self.head
        node = Node(data)
        for i in range(index-1):
            temp = temp.next
        node.next = temp.next
        temp.next = node
    def delete_begin(self):
        if self.head is None:
            print("linked list empty")
            return
        self.head = self.head.next
    def delete_end(self):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp1 = temp
            temp = temp.next
        temp1.next = None
    def delete_value(self, value):
        if self.head.data == value:
            self.head = self.head.next
        temp = self.head
        while temp.data != value and temp.next is not None:
            temp = temp.next
        