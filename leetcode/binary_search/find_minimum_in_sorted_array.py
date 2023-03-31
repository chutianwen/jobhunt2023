class Solution:
    def findMin(self, nums) -> int:
        '''
        case 1: pivot on the right half
        +++++++++----
        case 2: pivot on the left half
        ++++---------
        case 2: No rotation
        -------------
        :param nums:
        :return: 
        '''
        end = len(nums)
        lo, hi = 0, end - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            # print(f'lo:{nums[lo]}, mid:{nums[mid]}, hi:{nums[hi]}')
            if end-1 > mid > 0 and nums[mid - 1] > nums[mid] and nums[mid + 1] > nums[mid]:
                return nums[mid]
            elif nums[mid] > nums[hi]:
                # target must be on the right part
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                if nums[mid] < nums[lo]:
                    hi = mid - 1
                else:
                    # no rotation at all
                    return nums[lo]
            else:
                # mid == hi
                return nums[mid]


class OptimizedSolution:
    def findMin(self, nums) -> int:
        end = len(nums)
        lo, hi = 0, end - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            print(f'lo:{nums[lo]}, mid:{nums[mid]}, hi:{nums[hi]}')

            # +++++++++----
            if nums[mid] > nums[hi]:
                lo = mid + 1
            # ++++---------
            elif nums[mid] < nums[lo]:
                hi = mid
            else:
                return nums[lo]


class Solution2:
    def findMin(self, nums) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_value = self.fun(nums, mid)
            print(f'left:{left}, mid:{mid}, right:{right}')
            if mid_value > nums[right]:
                left = mid + 1
            elif mid_value < nums[left]:
                right = mid
            elif nums[left] <= mid_value <= nums[right]:
                return nums[left]
            else:
                print('ddd')
        return nums[left]

    def fun(self, nums, x):
        return nums[x]


nums = [2]
s = Solution2()
print(s.findMin(nums))


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_value = self.fun(arr, mid, x)
            mid_k_value = arr[mid + k] - x  # self.fun(arr, mid + k, x)
            # print(f'left:{left}, mid:{mid}, right:{right}')

            # print(x-arr[mid], self.fun(arr, mid, x), arr[mid + k] - x, self.fun(arr, mid + k, x))
            # print(f'mid_value:{mid_value}, mid_k_value:{mid_k_value}')
            if mid_value > mid_k_value:
                left = mid + 1
            elif mid_value < mid_k_value:
                right = mid - 1
            elif mid_value == mid_k_value:
                right = mid - 1

        return arr[left: left + k]

    def fun(self, nums, idx, x):
        return abs(nums[idx] - x)