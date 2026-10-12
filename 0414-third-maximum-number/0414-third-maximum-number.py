class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        lst1 = list(set(nums))

        lst1.sort()
        if len(lst1) < 3:
            return max(lst1)
        else:
            return lst1[-3]

        