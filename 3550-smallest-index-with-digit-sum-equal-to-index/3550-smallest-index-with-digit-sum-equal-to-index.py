class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            total = 0
            while nums[i]:
                total += nums[i] % 10
                nums[i] //= 10
            
            if total == i:
                return i
        return -1 