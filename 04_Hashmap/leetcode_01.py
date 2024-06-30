# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}

        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in hashmap:
                return [i, hashmap[remaining]]
            hashmap[nums[i]] = i
