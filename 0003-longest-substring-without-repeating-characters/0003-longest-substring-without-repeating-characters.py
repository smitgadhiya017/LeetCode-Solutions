class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1 = set()
        left = 0
        maxi = 0

        for right in range(len(s)):
            while s[right] in set1:
                set1.remove(s[left])
                left += 1

            set1.add(s[right])
            maxi = max(maxi, right - left + 1)
        
        return maxi