from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        buffer = deque([])

        res = []
        for idx, num in enumerate(nums):
            while buffer and buffer[-1] < num:
                buffer.pop()

            buffer.append(num)

            if idx >= k - 1:
                res.append(buffer[0])
                left = nums[idx - k + 1]
                if left == buffer[0]:
                    buffer.popleft()

        return res