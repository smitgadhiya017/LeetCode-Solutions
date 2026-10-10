class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = defaultdict(int)

        for i in nums:
            ans[i] += 1

        for n,c in ans.items():
            if c == 1:
                return n
        