class Solution:
    def findMin(self, nums: List[int]) -> int:
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