class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str1 = s.strip()
        c = 0
        for i in range(len(str1)-1,-1,-1):
            if str1[i] != ' ':
                c += 1
            else: 
                break
        return c