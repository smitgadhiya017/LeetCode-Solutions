class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = -100000

        for i in range(len(nums)):
            currSum += nums[i]
            maxSum = max(currSum, maxSum)

            if currSum < 0:
                currSum = 0

        return maxSum