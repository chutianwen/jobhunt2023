from collections import defaultdict


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return []

        explored = defaultdict(list)
        sorted_nums = sorted(nums)
        end = len(nums)

        def helper(start):
            if start == end:
                return []
            if start in explored:
                return explored[start]

            res = []
            for next_start in range(start, end):
                if next_start > start and sorted_nums[next_start] == sorted_nums[next_start - 1]:
                    continue
                res.append([sorted_nums[next_start]])
                subsets = helper(next_start + 1)
                res.extend(map(lambda subset: [sorted_nums[next_start]] + subset, subsets))
            explored[start] = res

            return res

        return [[]] + helper(0)