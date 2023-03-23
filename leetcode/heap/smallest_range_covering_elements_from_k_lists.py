import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        if not nums:
            return []
        # maintain a heap keeps all the frontier node at each list, coupled with the kth index. Calculate
        # max and min in the heap as the interval, until one list get exhausted.
        # num, ith_list
        frontier = []
        max_frontier = float('-inf')
        min_range = float('inf')

        list_indexes = [0 for _ in nums]
        list_index_limit = [len(sub_list) for sub_list in nums]

        for idx, sub_list in enumerate(nums):
            max_frontier = max(max_frontier, sub_list[0])
            heapq.heappush(frontier, (sub_list[0], idx))

        answer = []
        while list_indexes[frontier[0][1]] < list_index_limit[frontier[0][1]]:
            pre_min_frontier, min_idx = heapq.heappop(frontier)
            if (max_frontier - pre_min_frontier) < min_range:
                min_range = max_frontier - pre_min_frontier
                answer = [pre_min_frontier, max_frontier]

            list_indexes[min_idx] += 1
            if list_indexes[min_idx] == list_index_limit[min_idx]:
                break
            candidate = nums[min_idx][list_indexes[min_idx]]
            max_frontier = max(max_frontier, candidate)
            heapq.heappush(frontier, (candidate, min_idx))

        return answer

