class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        set1 = set(nums)
        for i in range(1,len(set1)+2):
            if i not in set1:
                return i