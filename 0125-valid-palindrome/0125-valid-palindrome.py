class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = ""

        for i in range(len(s)):
            if s[i].isalnum():
                str1 += s[i].lower()

        return str1 == str1[::-1]