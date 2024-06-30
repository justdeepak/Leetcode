# https://leetcode.com/problems/intersection-of-two-arrays/

from typing import List


class Solution:
    def get_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]

    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def intersection(self, nums1, nums2):
        # num1set = set(nums1)
        # num2set = set(nums2)

        # if len(num1set) < len(num2set):
        #     return self.get_intersection(num1set, num2set)
        # else:
        #     return self.get_intersection(num2set, num1set)

        setDict = {}
        for i in nums1:
            if i not in setDict:
                setDict[i] = i

        returnSet = set()
        for j in nums2:
            if j in setDict:
                returnSet.add(j)

        print(returnSet)


# if __name__ == "__main__":
#     test = Solution()
#     test.intersection(['red', 'blue', 'pink', 'purple'],
#                       ['blue', 'black', 'red'])
