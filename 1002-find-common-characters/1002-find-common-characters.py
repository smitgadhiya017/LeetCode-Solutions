from collections import *
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])

        for word in words[1:]:
            current = Counter(word)

            for ch in list(common.keys()):
                common[ch] = min(common[ch], current[ch])

                if common[ch] == 0:
                    del common[ch]
        
        return list(common.elements())
