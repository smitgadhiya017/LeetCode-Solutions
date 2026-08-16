class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxi = max(nums)
        c = 0
        for i in nums:
            if i != maxi:
                if maxi >= i * 2:
                    c += 1
        if c == len(nums)-1:
            for i in range(len(nums)):
                if maxi == nums[i]:
                    return i
                
        return -1