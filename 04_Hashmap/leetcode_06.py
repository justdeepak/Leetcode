# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        y = {0: 1}
        currentSum = 0
        returnVal = 0

        for idx, val in enumerate(nums):
            currentSum += val
            y_minus_k = currentSum - k
            if y_minus_k in y:
                returnVal += y[y_minus_k]

            if currentSum in y:
                y[currentSum] += 1
            else:
                y[currentSum] = 1

        print(returnVal)

if __name__ == "__main__":
    # arr = [2, 9, -2, 4, 1, -7, 2, 6, -5, 8, -3, -7, 6, 2, 1]
    # k = 5
    arr = [1,1,1]
    k = 2
    test = Solution()
    test.subarraySum(arr, k)