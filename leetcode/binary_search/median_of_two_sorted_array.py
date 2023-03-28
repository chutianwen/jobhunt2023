class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        size_1 = len(nums1)
        size_2 = len(nums2)

        if size_1 < size_2:
            small, large = nums1, nums2
            small_len, large_len = size_1, size_2
        else:
            small, large = nums2, nums1
            small_len, large_len = size_2, size_1

        # number of entries till the first median candidate
        mid_len = (small_len + large_len + 1) // 2
        # we are tracking the range of larger candidate for small nums
        lo = 0
        hi = small_len

        print(small, large, small_len, large_len)
        while lo <= hi:
            ## Candidates fall into small[small_mid - 1], small[mid], large[mid], large[mid - 1]
            # pointer to larger candidate from small nums
            small_mid = (lo + hi) // 2
            # pointer to the larger candidate from large nums
            large_mid = mid_len - small_mid

            if small_mid > 0 and small[small_mid - 1] > large[large_mid]:
                hi = small_mid - 1
            elif small_mid < small_len and small[small_mid] < large[large_mid - 1]:
                lo = small_mid + 1
            else:
                # exhaust small nums
                if small_mid == 0:
                    max_left = large[large_mid - 1]
                elif large_mid == 0:
                    max_left = small[small_mid - 1]
                else:
                    max_left = max(small[small_mid - 1], large[large_mid - 1])

                if (small_len + large_len) & 1:
                    return max_left

                if small_mid == small_len:
                    min_right = large[large_mid]
                elif large_mid == large_len:
                    min_right = small[small_mid]
                else:
                    min_right = min(small[small_mid], large[large_mid])

                return (max_left + min_right) / 2