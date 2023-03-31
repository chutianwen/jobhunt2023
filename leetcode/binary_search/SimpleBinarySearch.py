import bisect

def binary_search(nums, target):
    low = 0
    hi = len(nums) - 1
    while low <= hi:
        mid = (low + hi) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            hi = mid - 1
        else:
            low = mid + 1

    return low


def binary_search_left_inclusive(nums, target):
    low = 0
    hi = len(nums) - 1
    while low <= hi:
        # search between [low, hi]
        mid = low + (hi - low) // 2
        if nums[mid] >= target:
            hi = mid - 1
        else:
            low = mid + 1
    return low


def binary_search_left_exclusive(nums, target):
    low = 0
    hi = len(nums)
    while low < hi:
        # search between [low, hi)
        mid = low + (hi - low) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            low = mid + 1
    return low


def binary_search_right_inclusive(nums, target):
    low = 0
    hi = len(nums) - 1
    while low <= hi:
        mid = low + (hi - low) // 2
        # print(low, hi, mid)
        if nums[mid] > target:
            hi = mid - 1
        else:
            low = mid + 1

    return hi


def binary_search_right_exclusive(nums, target):
    low = 0
    hi = len(nums)
    while low < hi:
        mid = low + (hi - low) // 2
        # print(low, hi, mid)
        if nums[mid] > target:
            hi = mid
        elif nums[mid] == target:
            low = mid + 1
        elif nums[mid] < target:
            low = mid + 1

    return low

nums = [1,2,4,4,4,4,4,7,9]
target = 4
print(f'binary_search: {binary_search(nums, target)}')
print(f'binary_search_left_inclusive: {binary_search_left_inclusive(nums, target)}')
print(f'binary_search_left_exclusive: {binary_search_left_exclusive(nums, target)}')
print(f'bisect.bisect_left: {bisect.bisect_left(nums, target)}')
print(f'binary_search_right_inclusive: {binary_search_right_inclusive(nums, target)}')
print(f'binary_search_right_exclusive: {binary_search_right_exclusive(nums, target)}')
print(f'bisect.bisect_right: {bisect.bisect_right(nums, target)}')

nums.insert(binary_search_left_inclusive(nums, target), target)
print(nums)



