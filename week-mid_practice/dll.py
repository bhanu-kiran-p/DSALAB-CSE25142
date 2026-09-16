class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
    def insert_begin(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
    def insert_end(self,data):
        new = Node(data)
        if self.head is None:
            self.insert_begin(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
            new.prev = temp
    def insert_index(self, data, index):
        if index == 0:
            self.insert_begin(data)
            return
        if index < 0:
            print("no")
            return
        temp = self.head
        for i in range(index-1):
            if temp is None:
                print("not possible")
                return
            temp = temp.next
        if temp is None:
            print("not possible")
        else:
            new = Node(data)
            if temp.next:
                temp.next.prev = new
            new.next = temp.next
            new.prev = temp
            temp.next = new
    def delete_begin(self):
        if self.head is None:
            print("empty")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None
    def delete_end(self):
        if self.head is None:
            print("empty")
            return
        if self.head.next is None:
            self.head = None
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev = None
        temp.prev.next = None
    def delete_value(self, value):   # look into this later
        if self.head is None:
            self.delete_begin()
            return
        if self.head.data == value:
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
            return
        temp = self.head
        while temp.next:
            if self.head is None:
                print("value not found")
            if temp.data == value:
                break
            temp = temp.next
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
    def display_back(self):
        if self.head is None:
            print("Empty list")
        temp = self.head
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end="<->")
            temp = temp.prev