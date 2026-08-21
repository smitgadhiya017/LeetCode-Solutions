from collections import *
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        dict1 = defaultdict(int)

        for i in nums:
            dict1[i] += 1

        for n,c in dict1.items():
            # print(n,c)
            if c > 2:
                return False
        return True