class CircularQueue:

    def __init__(self, size) -> None:
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = -1

    def isEmpty(self) -> bool:
        if self.head == -1:
            return True
        return False

    def isFull(self) -> None:
        if self.tail + 1 % self.size == self.head:
            return True
        return False

    def enqueue(self, item) -> None:
        if self.isFull():
            print("Circular Queue Full")
            return

        if self.head == -1:
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = item
        print("Queued: {}".format(item))

    def dequeue(self) -> None:
        if self.isEmpty():
            print("Circular Queue Empty")
            return

        temp = self.queue[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        return temp


    def printQueue(self) -> None:
        if self.isEmpty():
            print("Queue Empty")
            return
        
        if self.head <= self.tail:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i])
        else:
            for i in range(self.head, self.size):
                print(self.queue[i])
            for i in range(0, self.tail + 1):
                print(self.queue[i])


if __name__ == "__main__":
    queue = CircularQueue(5)

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)

    print("Dequeued: {}".format(queue.dequeue()))
    print("Dequeued: {}".format(queue.dequeue()))

    queue.enqueue(60)
    queue.enqueue(70)
    queue.enqueue(80)
