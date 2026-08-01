class Solution(object):
    def findErrorNums(self, nums):
        s = set()
        duplicate = -1

        for i in nums:
            if i in s:
                duplicate = i
            s.add(i)

        for i in range(1,len(nums)+1):
            if i not in s:
                missing = i

        return [duplicate, missing]
