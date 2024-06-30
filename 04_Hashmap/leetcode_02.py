# https://leetcode.com/problems/group-anagrams/

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram = {}

        for i in strs:
            s = ""
            for j in sorted(i):
                s += j

            if s not in anagram:
                anagram[s] = []

            anagram[s].append(i)
        return list(anagram.values())
