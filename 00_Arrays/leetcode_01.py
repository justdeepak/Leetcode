# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in hashmap:
                return [i, hashmap[remaining]]
            hashmap[num] = i


if __name__ == "__main__":
    arr = [2,7,11,15]
    target = 9

    test = Solution()
    response = test.twoSum(arr, target)

    print(response)
