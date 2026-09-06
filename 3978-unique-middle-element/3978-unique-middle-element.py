class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid = len(nums) // 2
        for i in range(len(nums)):
            if nums[i] == nums[mid]:
                ans = nums[mid]
                nums.remove(nums[mid]) 
                break
        if ans in nums:
            return False
        return True