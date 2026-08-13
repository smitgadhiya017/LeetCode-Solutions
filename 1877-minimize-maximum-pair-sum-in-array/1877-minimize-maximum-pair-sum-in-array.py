class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxi = -100
        l = 0
        r = len(nums) - 1
        while l < r:
            total = nums[l] + nums[r]
            maxi = max(maxi,total)
            l += 1
            r -= 1
        return maxi 