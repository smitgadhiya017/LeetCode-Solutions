class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        count = 0
        for i in range(len(s)):
            for j in range(i,len(words)):
                word = words[j]
                for k in range(len(word)):
                    if word[k] == s[i]:
                        count += 1
                    break
                break
        return count == len(words) and count == len(s)