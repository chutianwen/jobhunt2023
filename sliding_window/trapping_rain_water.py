'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
it can trap after raining.

'''


class Solution:
    def trap(self, height: List[int]) -> int:

        # traverse left to right to get the max left at each position i.
        left_heights = []
        max_left = -1
        for left_height in height:
            max_left = max(max_left, left_height)
            left_heights.append(max_left)

        right_heights = []
        max_right = -1
        for right_height in height[::-1]:
            max_right = max(max_right, right_height)
            right_heights.append(max_right)
        right_heights.reverse()

        total_amount = 0
        for idx, cur_height in enumerate(height):
            total_amount += min(left_heights[idx], right_heights[idx]) - cur_height

        return total_amount