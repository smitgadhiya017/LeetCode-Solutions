class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            sqr = nums[i] * nums[i]
            ans.append(sqr)
        ans.sort()
        return ans