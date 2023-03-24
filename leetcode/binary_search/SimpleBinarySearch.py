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


def binary_search_left(nums, target):
    low = 0
    hi = len(nums) - 1
    while low <= hi:
        mid = (low + hi) // 2
        if target == nums[mid]:
            if mid > 0 and nums[mid - 1] < target:
                return mid
            if mid == 0:
                return mid
            hi = mid - 1
        elif target < nums[mid]:
            hi = mid - 1
        else:
            low = mid + 1
    return low

def binary_search_right(nums, target):
    low = 0
    hi = len(nums) - 1
    while low <= hi:
        mid = (low + hi) // 2
        print(low, hi, mid)
        if target == nums[mid]:
            if mid < len(nums) - 1 and nums[mid + 1] > target:
                return mid + 1
            if mid == len(nums) - 1:
                return mid + 1
            low = mid + 1
        elif target < nums[mid]:
            hi = mid - 1
        else:
            low = mid + 1
    return low

nums = [1,2,4,4,4,4,4,7,9]
target = 4
print(f'binary_search: {binary_search(nums, target)}')
print(f'binary_search_left: {binary_search_left(nums, target)}')
print(f'bisect.bisect_left: {bisect.bisect_left(nums, target)}')
print(f'binary_search_right: {binary_search_right(nums, target)}')
print(f'bisect.bisect_right: {bisect.bisect_right(nums, target)}')

nums.insert(binary_search_left(nums, target), target)
print(nums)