from collections import *
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        dict1 = defaultdict(int)
        n = len(candyType) // 2
        for i in candyType:
            dict1[i] += 1

        return min(n, len(dict1))