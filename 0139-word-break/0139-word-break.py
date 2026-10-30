class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        word_lengths = set(map(len, words))
        visited = set()

        def check(start):
            if start == len(s):
                return True

            if start in visited:
                return False

            visited.add(start)

            for length in word_lengths:
                end = start + length

                if end <= len(s) and s[start:end] in words:
                    if check(end):
                        return True

            return False

        return check(0)