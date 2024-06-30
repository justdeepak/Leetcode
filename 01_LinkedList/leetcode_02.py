# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    def checkForCycle(self, head):
        
        slow, fast = head, head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return slow
        
        return None
    
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        
        intersection = self.checkForCycle(head)
        if intersection is None:
            return None
        
        first = intersection
        second = head
        
        while first != second:
            first = first.next
            second = second.next
        
        return first
            
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
    response = test.detectCycle(head)
    print("Meets at value: {}".format(response.val))