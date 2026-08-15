class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = defaultdict(int)
        
        for i in nums:
            ans[i] += 1

        for i in nums:
            if ans[i] == 1:
                return i