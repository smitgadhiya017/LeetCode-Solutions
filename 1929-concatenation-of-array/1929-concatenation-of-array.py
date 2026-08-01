class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(len(nums)):
            lst.append(nums[i])
        for i in range(len(nums)):
            lst.append(nums[i])
        return lst