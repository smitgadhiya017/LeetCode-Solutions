class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxi = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            maxi = max(maxi, curr_max)
        
        return maxi