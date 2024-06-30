# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        returnList = ListNode(0)
        current = returnList
        sumOverNine = 0
        
        while l1 is not None or l2 is not None or sumOverNine > 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
                
            nodeSum = l1Val + l2Val + sumOverNine
            sumOverNine = nodeSum // 10
            
            newNode = ListNode(nodeSum % 10)
            current.next = newNode
            
            current = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return returnList.next

if __name__ == "__main__":
    head_1 = ListNode(8)
    second_1 = ListNode(1)
    third_1 = ListNode(2)

    head_2 = ListNode(5)
    second_2 = ListNode(2)
    third_2 = ListNode(3)

    head_1.next = second_1
    second_1.next = third_1
    
    head_2.next = second_2
    second_2.next = third_2

    test = Solution()
    response = test.addTwoNumbers(head_1, head_2)
    print(response.val)
    while response.next is not None:
        response = response.next
        print(response.val)            