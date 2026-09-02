from collections import *
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s = str(n)
        freq = defaultdict(int)
        
        for i in s:
            freq[i] += 1
        
        ans = 0
        for k,v in freq.items():
            ans += int(k) * v

        return ans