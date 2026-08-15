from collections import Counter 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for n,c in freq.items():
            if c == 1:
                return n