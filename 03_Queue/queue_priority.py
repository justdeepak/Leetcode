class PriorityQueue:

    def __init__(self):
        pass

    def _heapify(self, arr, n, i):
        # Find the largest node, left child and right child
        largest = i
        # i starts from 0
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            largest = left

        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self._heapify(arr, n, largest)

    def insert(self, arr, newNum):
        size = len(arr)
        arr.append(newNum)
        if size > 0:
            for i in range((size // 2) - 1, -1, -1):
                self._heapify(arr, size, i)

    def deleteNode(self, arr, num):
        size = len(arr)
        i = 0

        for i in range(0, size):
            if num == arr[i]:
                break

        arr[i], arr[size - 1] = arr[size - 1], arr[i]

        arr.remove(size - 1)

        for i in range((size // 2) - 1, -1, -1):
            self._heapify(arr, len(arr), i)


if __name__ == "__main__":
    priorityQueue = PriorityQueue()

    arr = []
    priorityQueue.insert(arr, 3)
    priorityQueue.insert(arr, 4)
    priorityQueue.insert(arr, 9)
    priorityQueue.insert(arr, 5)
    priorityQueue.insert(arr, 2)

    print("Heap array: {}".format(arr))

    priorityQueue.deleteNode(arr, 4)
    print("Heap array after deleting an element: {}".format(arr))
    