class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        total = nums[0]
        maxi = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                total += nums[i]
            else:
                total = nums[i]
            maxi = max(maxi, total)

        return maxi 