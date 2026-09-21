class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def create(self):
        n = int(input("Enter no of nodes: "))
        for i in range(n):
            new = Node(int(input("Enter the data: ")))
            if self.head is None:
                self.head = new
                self.tail = new
                return 
            self.tail.next = new
            self.tail = new
            self.tail.next = self.head
        print("circular linked list created successfully.")
    def insert_begin(self, data):
        new = Node(data)
        if self.head is None:
            self.head = self.tail = new
            return
        self.tail.next = new
        new.next = self.head
        self.head = new
        print("data inserted successfullly")
        return
    def insert_end(self,data):
        new = Node(data)
        if self.head is None:
            self.insert_begin(data)
            return
        self.tail.next = new
        new.next = self.head
        self.tail = new
        print("data inserted successfully")
        return
    def delete_begin(self):
        if self.head is None:
            print("the list is empty")
            return
        if self.head == self.tail:
            self.head = self.tial= 
            n