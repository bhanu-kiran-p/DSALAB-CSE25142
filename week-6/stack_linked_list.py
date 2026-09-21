class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    def push(self,item):
        # since we use linked list, there is no over flow condition
        node = Node(item)
        if self.top is None:
            self.top = node
            return
        node.next = self.top
        self.top = node
        print(f"{item} inserted")
    def pop(self):
        # checking for the under flow condition
        if self.top is None:
            print("stack is empty")
            return
        #need to give the self.top to  the next node
        item = self.top.data
        self.top = self.top.next
        print(f"{item} removed")
    def peek(self):
        # checking if the list is empty
        if self.top is None:
            print("stack is none")
            return
        # display the top node data
        print(f"{self.top.data} is the top item")
    def display(self):
        # checking if hte stack is empty
        if self.top is None:
            print("stack is empty")
            return
        temp = self.top
        while temp:
            print(f"{temp.data}", end='->')
            temp = temp.next
        print("None")

def main():
    stack = Stack()
if __name__ =='__main__':
    main()