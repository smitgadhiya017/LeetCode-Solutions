class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        c = 0

        for i in nums:
            if c < 2 or i != nums[c - 2]:
                nums[c] = i
                c += 1

        return c