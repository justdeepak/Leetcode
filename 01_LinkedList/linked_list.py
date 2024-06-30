class Node:
    def __init__(self, value = None):
        self.value = value
        self._next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

if __name__ == "__main__":
    head = Node(1)
    second = Node(2)
    third = Node(3)

    linkedList = LinkedList()
    linkedList.head = head
    linkedList.head._next = second
    second._next = third

    current = linkedList
    while current.head != None:
        print(current.head.value)
        current.head = current.head._next
        