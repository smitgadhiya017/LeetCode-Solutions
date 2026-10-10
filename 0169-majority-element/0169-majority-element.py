class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = defaultdict(int)

        for i in nums:
            ans[i] += 1

        maxi = 0
        for n,c in ans.items():
            maxi = max(maxi,c)

        for n,c in ans.items():
            if maxi == c:
                return n