class Solution:
    def splitArray(self, nums, k: int) -> int:

        low, hi = min(nums), sum(nums)
        target = k

        while low <= hi:
            mid = low + (hi - low) // 2
            num_splits = self.num_splits(mid, nums)
            if num_splits < target:
                low = num_splits + 1
            elif num_splits > target:
                hi = num_splits - 1
            elif num_splits == target:
                hi = num_splits - 1

        return low

    def num_splits(self, budget, nums):
        num_split = 0
        cur_budget = 0
        for num in nums:
            if cur_budget < num:
                cur_budget = budget
                num_split += 1

            cur_budget -= num

        return num_split


s = Solution()
nums = [7,2,5,10,8]
k = 2

print(s.num_splits(2, nums))
print(s.splitArray(nums, k))