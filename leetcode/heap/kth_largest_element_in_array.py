import heapq


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        # top k, from kth to 1st
        min_heap = []
        size_heap = 0
        for num in nums:
            if size_heap < k:
                heapq.heappush(min_heap, num)
                size_heap += 1
            else:
                if min_heap[0] < num:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, num)
        return min_heap[0]


class QuickSelectSolution(object):
    def findKthLargestRecursion(self, nums, k):
        end = len(nums)
        lo = 0
        hi = end - 1
        target_index = end - k

        def helper(start, end):
            if start > end:
                return None
            partition = self.partition(nums, start, end)
            if partition == target_index:
                return nums[partition]
            elif partition > target_index:
                return helper(start, partition - 1)
            else:
                return helper(partition + 1, end)

        res = helper(0, len(nums) - 1)
        return res

    def findKthLargest(self, nums, k):
        end = len(nums)
        lo = 0
        hi = end - 1
        target_index = end - k

        while lo <= hi:
            partition = self.partition(nums, lo, hi)
            # print(f'partition:{nums[partition]}, nums:{nums}, target_index:{target_index}, partition:{partition}')
            if partition == target_index:
                return nums[partition]
            elif partition > target_index:
                hi = partition - 1
            else:
                lo = partition + 1

        return 'problem'

    def partition(self, nums, lo, hi):
        cur_lo = lo
        cur_hi = hi - 1
        pivot = hi

        while cur_lo <= cur_hi:
            while cur_lo <= cur_hi and nums[cur_lo] <= nums[pivot]:
                cur_lo += 1
            while cur_lo <= cur_hi and nums[cur_hi] > nums[pivot]:
                cur_hi -= 1

            if cur_lo > cur_hi:
                break
            nums[cur_lo], nums[cur_hi] = nums[cur_hi], nums[cur_lo]

        # print(cur_lo, pivot)
        nums[cur_lo], nums[pivot] = nums[pivot], nums[cur_lo]
        return cur_lo


s = QuickSelectSolution()

nums = [1,2,3,4,5,6,7,8]
res = s.findKthLargest(nums, 1)
print(res, nums)
res1 = s.findKthLargestRecursion(nums, 1)
print(res1)