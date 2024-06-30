# https://leetcode.com/problems/valid-parentheses/submissions/

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
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        hashmap = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in hashmap:
                topelement = stack.pop() if not stack.check_empty() else '#'

                if hashmap[char] != topelement:
                    return False
            
            else:
                stack.push(char)

        return stack.check_empty()


if __name__ == "__main__":
    testString = "({})[]"
    test = Solution()
    print(test.isValid(testString))

    testString = "({})[]["
    print(test.isValid(testString))
