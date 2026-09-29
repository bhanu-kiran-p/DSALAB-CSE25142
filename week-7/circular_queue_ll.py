class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, item):
        node = Node(item)
        if self.rear is None:
            self.front = self.rear = node
            self.rear.next = self.front
            print(f"{item} inserted")
            return
        self.rear.next = node
        node.next = self.front
        self.rear = node
        print(f"{item} is inserted into circular queue")
        return
    def dequeue(self):
        if self.front is None:
            print("queue under flow")
            return
        item = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        print(f"{item} is deleted from queue")
        return
    def peek(self):
        if self.front is None:
            print("The circular queue is empty")
            return
        item = self.front.data
        print(f"{item} is the front element")
        return
    def display(self):
        if self.front is None:
            print("the queue is empty")
            return
        temp = self.front
        while temp!= self.rear:
            print(temp.data, end="|")
            temp = temp.next
        print(temp.data)
        return
    
def main():
    print("cse25142, bhanu kiran")
    queue = CircularQueue()
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
        
        