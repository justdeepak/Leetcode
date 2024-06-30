# https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # hashMap = {}

        # for val in s:
        #     if val in hashMap:
        #         hashMap[val] += 1
        #     else:
        #         hashMap[val] = 1
        hashMap = Counter(s)

        for idx, val in enumerate(s):
            if hashMap[val] == 1:
                return idx

        return -1
