from collections import deque


class Solution:
    def pathSum(self, nums) -> int:
        if not nums:
            return 0

        end = len(nums) - 1
        # element, cur_sum
        q = deque([(nums[0], nums[0] % 10)])
        idx = 1
        total_path_sum = 0

        while q:

            cur_element, cur_sum = q.popleft()
            cur_level = cur_element // 100
            cur_pos = cur_element // 10 % 10

            is_leaf = True
            # check children
            while idx <= end:
                next_level = nums[idx] // 100
                next_pos = nums[idx] // 10 % 10
                next_val = nums[idx] % 10
                if cur_level + 1 == next_level and next_pos in (cur_pos * 2 - 1, cur_pos * 2):
                    q.append((nums[idx], cur_sum + next_val))
                    is_leaf = False
                    idx += 1
                else:
                    break
            # if no children, means the branch, add the path
            # print(cur_level, cur_pos, cur_element % 10, cur_sum, is_leaf, idx)

            if is_leaf:
                total_path_sum += cur_sum

        return total_path_sum

