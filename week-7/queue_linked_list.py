class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        # since linked list has dynamic allocation no size required
    def enqueue(self, item):
        node = Node(item)
        # no over flow condition
        if self.front is None:
            self.rear = node
            self.front = node
            print(f"{item} inserted")
            return
        self.rear.next = node
        self.rear = node
        print(f"{item} is inserted")
        return
    def dequeue(self):
        # checking the under flow condition
        if self.front is None:
            print("queue under flow")
            return
        item = self.front.data
        self.front = self.front.next
        print(f"{item} is deleted")
        return
    def peek(self):
        if self.front is None:
            print("queue is empty")
            return
        item = self.front.data
        print(f"{item} is the front item")
        return
    def display(self):
        if self.front is None:
            print("queue is Empty")
            return
        temp = self.front
        while temp:
            print(temp.data, end=" | ")
            temp = temp.next
        print("")
        return
def main():
    print("cse25142, bhanu kiran")
    queue = Queue()
    while True:
        print("-"*10)
        print("1. enqueue\n2.dequeue\n3.peek\n4.display\n5.exit")
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            queue.enqueue(int(input("Enter the item: ")))
        elif choice == 2:
            queue.dequeue()
        elif choice == 3:
            queue.peek()
        elif choice == 4:
            queue.display()
        elif choice == 5:
            print("Exiting the program.....")
            break
        else:
            print("Invalid choice")
        
if __name__ == '__main__':
    main()
        
    