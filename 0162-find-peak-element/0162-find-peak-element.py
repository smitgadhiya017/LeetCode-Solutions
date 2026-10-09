class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        maxi = max(nums)

        for i in range(len(nums)):
            if nums[i] == maxi:
                return i