class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        ans = 0
        for i in range(k):
            ans += nums[i]

        for i in range(len(nums)-k,len(nums)):
            ans -= nums[i]

        return abs(ans)