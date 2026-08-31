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
    linkedList.reverse()
    linkedList.display()


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
        arr = []
        temp = self.head
        while temp:
            arr.append(temp)
            temp = temp.next
        for i in range(len(arr) - 1, -1, -1):
            print(arr[i].data, end="<->")
        print("None")


if __name__ == "__main__":
    main()
