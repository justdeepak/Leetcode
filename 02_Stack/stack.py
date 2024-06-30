class Stack:

    def __init__(self) -> None:
        self.stack = []

    def peek(self) -> int:
        if self.isEmpty():
            return None

        return self.stack[len(self.stack) - 1]

    def isEmpty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False

    def push(self, item):
        self.stack.append(item)
        print("pushed: {}".format(item))

    def pop(self) -> int:
        if self.isEmpty():
            return None
            
        return self.stack.pop()


if __name__ == "__main__":
    stack = Stack()
    stack.push(20)
    stack.push(30)
    stack.push(40)
    print("popped: {}".format(stack.pop()))
    stack.push(50)
    print("popped: {}".format(stack.pop()))
    print("popped: {}".format(stack.pop()))
    print("popped: {}".format(stack.pop()))