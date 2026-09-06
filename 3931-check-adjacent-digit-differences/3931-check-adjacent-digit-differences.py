class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        c = 0
        for i in range(len(s)-1):
            ans = abs(int(s[i])-int(s[i+1]))
            
            if ans <= 2:
                c += 1
        return c == len(s)-1
