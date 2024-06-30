# https://leetcode.com/problems/reverse-linked-list/solution/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self):
        self.stack = []

    def check_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.check_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.check_empty():
            return None

        return self.stack[len(self.stack) - 1]


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        current = head
        stack = Stack()

        while current is not None:
            stack.push(current.val)
            current = current.next

        returnList = ListNode(0)
        current = returnList

        while(not stack.check_empty()):
            newNode = ListNode(stack.pop())
            current.next = newNode
            current = current.next
        return returnList.next

    def reverseList2(self, head):
        if head is None or head.next is None:
            return head
        
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return p


if __name__ == "__main__":
    head = ListNode(3)
    second = ListNode(2)
    third = ListNode(0)
    fourth = ListNode(4)

    head.next = second
    second.next = third
    third.next = fourth

    test = Solution()
    response = test.reverseList(head)
    
    print(response.val)
    while response.next is not None:
        response = response.next
        print(response.val)

    response = test.reverseList(head)

    # print(response.val)
    # while response.next is not None:
    #     response = response.next
    #     print(response.val)