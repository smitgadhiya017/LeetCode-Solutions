class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq = {}

        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        for n,c in freq.items():
            if c == 1:
                return n