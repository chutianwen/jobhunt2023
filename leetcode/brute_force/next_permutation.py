class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end = len(nums) - 1
        pivot = None
        right = end
        while right >= 1:
            if nums[right] > nums[right - 1]:
                pivot = right - 1
                break
            else:
                right -= 1

        if not pivot:
            return nums[::-1]

        right = end
        while right > pivot:
            if nums[right] > nums[pivot]:
                nums[right], nums[pivot] = nums[pivot], nums[right]
                break
            else:
                right -= 1

        return nums[::-1]


s = Solution()

r = s.nextPermutation([3,2,1])
print(r)