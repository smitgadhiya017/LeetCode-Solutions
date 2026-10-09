class Solution:
    def reverseWords(self, s: str) -> str:        
        str1 = str.split(s)
        return ' '.join(str1[::-1])