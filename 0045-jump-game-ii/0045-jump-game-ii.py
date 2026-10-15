class Solution:
    def jump(self, nums: list[int]) -> int:
        ans = 0
        current_end = 0
        maxi = 0

        for i in range(len(nums) - 1):
            maxi = max(maxi, i + nums[i])

            if i == current_end:
                ans += 1
                current_end = maxi

        return ans
