class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if not nums or len(nums) == 1:
            return True

        end = len(nums)
        max_jumps_budget = 0

        for idx in range(0, end):
            if idx == 0:
                max_jumps_budget = nums[idx]
            else:
                max_jumps_budget = max(max_jumps_budget - 1, nums[idx])
            if max_jumps_budget == 0 and idx < end - 1:
                return False
        return True
