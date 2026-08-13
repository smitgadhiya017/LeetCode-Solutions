class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        maxi = max(nums)
        mini = min(nums)
        ans = 0
        for i in range(1,mini+1):
            if mini % i == 0 and maxi % i == 0:
                ans = i

        return ans