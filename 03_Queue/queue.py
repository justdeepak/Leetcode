class Queue:

    def __init__(self) -> None:
        self.queue = []

    def isEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False

    def display(self):
        print(self.queue)

    def peek(self):
        if self.isEmpty():
            return None
        
        return self.queue[len(self.queue) - 1]

    def enqueue(self, item) -> None:
        self.queue.append(item)
        print("Enqueued: {}".format(item))
    
    def dequeue(self) -> int:
        if self.isEmpty():
            return None
        return self.queue.pop(0)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)

    print("Dequeued: {}".format(queue.dequeue()))
    print("Dequeued: {}".format(queue.dequeue()))
    print("Dequeued: {}".format(queue.dequeue()))
    print("Dequeued: {}".format(queue.dequeue()))