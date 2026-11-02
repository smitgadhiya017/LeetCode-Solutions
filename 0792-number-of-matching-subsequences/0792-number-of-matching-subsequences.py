from collections import defaultdict
from bisect import bisect_right

class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        positions = defaultdict(list)

        for i, char in enumerate(s):
            positions[char].append(i)

        count = 0

        for word in words:
            prev = -1
            found = True

            for char in word:
                indexes = positions[char]

                j = bisect_right(indexes, prev)

                if j == len(indexes):
                    found = False
                    break

                prev = indexes[j]

            if found:
                count += 1

        return count