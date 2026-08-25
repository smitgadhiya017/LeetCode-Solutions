class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        set1 = set(nums)
        ans = k
        while ans in set1:
            ans += k
        return ans