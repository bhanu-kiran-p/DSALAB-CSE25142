def main():
    linkedList = LinkedList()
    linkedList.add(2)
    linkedList.add(3)
    linkedList.add(10)
    linkedList.add(13)
    linkedList.add(90)
    print("Forward:")
    linkedList.display()
    print("Reverse:")
    linkedList.display_rev()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="<->")
            temp = temp.next
        print("None")
    def display_rev(self):
        temp = 

if __name__ == '__main__':
    main()
