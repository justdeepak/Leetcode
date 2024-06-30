# https://leetcode.com/problems/top-k-frequent-elements/

import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return nums

        counter = {}
        for i in nums:
            counter[i] = counter[i] + 1 if i in counter else 1

        return heapq.nlargest(k, counter.keys(), key=counter.get)
