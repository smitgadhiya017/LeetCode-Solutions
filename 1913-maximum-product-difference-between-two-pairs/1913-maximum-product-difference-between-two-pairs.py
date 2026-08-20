class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        total = 1
        n = len(nums)-1
        i = 0
        total = (nums[n] * nums[n-1]) - (nums[i] * nums[i+1])

        return total