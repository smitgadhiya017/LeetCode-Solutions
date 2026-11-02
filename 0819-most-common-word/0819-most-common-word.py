import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = re.findall(r"[a-zA-Z]+", paragraph.lower())

        banned_set = set(banned)

        valid_words = []

        for word in words:
            if word not in banned_set:
                valid_words.append(word)

        counts = Counter(valid_words)

        return counts.most_common(1)[0][0]