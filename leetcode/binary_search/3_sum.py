class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        end = len(nums)
        res = []

        def calculate(n, target, cur_nums, start):
            if n < 2 or start > end - n or nums[start] * n > target or nums[end - 1] * n < target:
                return

            if n == 2:
                lo = start
                hi = end - 1
                while lo < hi:
                    value = nums[lo] + nums[hi]
                    if value < target:
                        lo += 1
                    elif value > target:
                        hi -= 1
                    else:
                        res.append(cur_nums + [nums[lo], nums[hi]])
                        while lo < end - 1 and nums[lo] == nums[lo + 1]:
                            lo += 1
                        lo += 1
                        while hi > start and nums[hi] == nums[hi - 1]:
                            hi -= 1
                        hi -= 1
            else:
                for next_start in range(start, end):
                    if next_start == start or nums[next_start] != nums[next_start - 1]:
                        calculate(n - 1, target - nums[next_start], cur_nums + [nums[next_start]], next_start + 1)

        calculate(3, 0, [], 0)
        return res