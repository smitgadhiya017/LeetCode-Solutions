class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        ans = defaultdict(int)
        n = len(nums) // 2
    
        for i in nums:
            ans[i] += 1

        for i in nums:
            if ans[i] == n:
                return i
            