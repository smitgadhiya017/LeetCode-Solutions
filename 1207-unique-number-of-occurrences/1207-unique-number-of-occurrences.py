from collections import *
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict1 = defaultdict(int)

        for i in arr:
            dict1[i] += 1

        lst = []
        for i,c in dict1.items():
            lst.append(c)
        
        lst.sort()
        if len(lst) == 1:
            return True

        for i in range(len(lst)-1):
            if lst[i] == lst[i+1]:
                return False
        return True