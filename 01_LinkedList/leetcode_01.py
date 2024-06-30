# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        
        slow, fast = head, head.next
        
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            
            slow = slow.next
            fast = fast.next.next
        
        return True

if __name__ == "__main__":
    head = ListNode(3)
    second = ListNode(2)
    third = ListNode(0)
    fourth = ListNode(4)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = second

    test = Solution()
    response = test.hasCycle(head)
    print(response)