def left_bound_inclusive(nums, target):
    left, right = 0, len(nums) - 1

    def function(nums, x):
        '''
        function must be monolithic up or down
        '''
        return nums[x]

    while left <= right:
        mid = left + (right - left) // 2
        mid_value = function(nums, mid)
        if target > mid_value:
            left = mid + 1
        elif target <= mid_value:
            right = mid - 1

    left_bound_target_index = -1 if left == len(nums) or nums[left] != target else left
    return left_bound_target_index, left


def right_bound_inclusive(nums, target):
    left, right = 0, len(nums) - 1

    def function(nums, x):
        '''
        function must be monolithic up or down
        '''
        return nums[x]

    while left <= right:
        mid = left + (right - left) // 2
        mid_value = function(nums, mid)
        if target >= mid_value:
            left = mid + 1
        elif target < mid_value:
            right = mid - 1

    right_bound_target_index = -1 if right < 0 or nums[right] != target else right
    return right_bound_target_index, right + 1


nums = [1, 2, 4, 4, 4, 4, 4, 7, 9]
target = 5

left_bound_target_index, num_entry_small_than_target = left_bound_inclusive(nums, target)
right_bound_target_index, num_entry_small_equal_than_target = right_bound_inclusive(nums, target)
print(f'left_bound_inclusive: num_entry_small_than_target:{num_entry_small_than_target}, left_bound_target_index:{left_bound_target_index}')
print(f'right_bound_inclusive: num_entry_small_equal_than_target:{num_entry_small_equal_than_target}, right_bound_target_index:{right_bound_target_index}')