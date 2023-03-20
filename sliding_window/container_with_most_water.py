class Solution:
    def maxArea(self, height: List[int]) -> int:
        end = len(height)
        left = 0
        right = end - 1
        max_amount = 0
        while left < right:
            cur_width = right - left
            if height[left] < height[right]:
                cur_height = height[left]
                new_left = left + 1
                while new_left < end and height[left] >= height[new_left]:
                    new_left += 1
                left = new_left
            else:
                cur_height = height[right]
                new_right = right - 1
                while new_right >= 0 and height[right] >= height[new_right]:
                    new_right -= 1
                right = new_right

            cur_amount = cur_width * cur_height
            max_amount = max(max_amount, cur_amount)

            # print(cur_amount)

        return max_amount
