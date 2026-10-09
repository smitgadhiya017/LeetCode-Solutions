class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        find = set()
        ans = []
        for i in range(len(nums)):
            if nums[i] in find:
                ans.append(nums[i])
                continue

            find.add(nums[i])
        return ans