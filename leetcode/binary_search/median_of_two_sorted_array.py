class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) <= len(nums2):
            shorter, longer, shorter_len, longer_len = nums1, nums2, len(nums1), len(nums2)
        else:
            shorter, longer, shorter_len, longer_len = nums2, nums1, len(nums2), len(nums1)

        # first candidate index, 1 based (3, 4) => 4, (4, 4) => (4, 5)
        mid_length = (shorter_len + longer_len + 1) // 2

        # range of number of used elements from shorter, use nothing or use all
        lo, hi = 0, shorter_len

        while lo <= hi:
            # how many short values used
            short_used_len = lo + (hi - lo) // 2
            long_used_len = mid_length - short_used_len

            # compare short_mid - 1, and long_mid - 1
            if short_used_len >= 1 and shorter[short_used_len - 1] > longer[long_used_len]:
                hi = short_used_len - 1
            elif short_used_len < shorter_len and shorter[short_used_len] < longer[long_used_len - 1]:
                lo = short_used_len + 1
            else:
                if short_used_len == 0:
                    max_left = longer[long_used_len - 1]
                elif long_used_len == 0:
                    max_left = shorter[short_used_len - 1]
                else:
                    max_left = max(shorter[short_used_len - 1], longer[long_used_len - 1])

                if (shorter_len + longer_len) & 1:
                    return max_left

                if short_used_len == shorter_len:
                    min_right = longer[long_used_len]
                elif long_used_len == longer_len:
                    min_right = shorter[short_used_len]
                else:
                    min_right = min(shorter[short_used_len], longer[long_used_len])
                return (max_left + min_right) / 2
