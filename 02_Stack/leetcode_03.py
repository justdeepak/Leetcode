# https://leetcode.com/problems/largest-rectangle-in-histogram/

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            stack.append(i)

        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)

        return max_area

    #     def largestRectangleArea(self, heights: List[int]) -> int:
    #         return self.calculateArea(heights, 0, len(heights) - 1)

    #     def calculateArea(self, heights: List[int], start: int, end: int) -> int:
    #         if start > end:
    #             return 0

    #         min_index = start
    #         for i in range(start, end + 1):
    #             if heights[min_index] > heights[i]:
    #                 min_index = i

    #         return max(
    #             self.calculateArea(heights, start, min_index - 1),
    #             self.calculateArea(heights, min_index + 1, end),
    #             heights[min_index] * (end - start + 1),
    #         )
