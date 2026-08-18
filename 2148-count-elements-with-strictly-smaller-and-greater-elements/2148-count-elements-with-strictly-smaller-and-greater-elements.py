class Solution:
    def countElements(self, nums: List[int]) -> int:
        c = 0
        maxi = max(nums)
        mini = min(nums)
        for i in range(len(nums)):
            if nums[i] == maxi or nums[i] == mini:
                continue
            c += 1
        return c