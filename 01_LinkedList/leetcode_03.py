# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newhead = ListNode(0, head)
        pred = newhead
        
        while head:
            
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                    
                pred.next = head.next
                
            else:
                pred = pred.next
                
            head = head.next
        
        # Return the newhead linked list without the new root node
        return newhead.next


if __name__ == "__main__":
    head = ListNode(1)
    second = ListNode(1)
    third = ListNode(2)
    fourth = ListNode(2)

    head.next = second
    second.next = third
    third.next = fourth

    test = Solution()
    response = test.deleteDuplicates(head)

    print(response.val)
    while response.next is not None:
        response = response.next
        print(response.val)
