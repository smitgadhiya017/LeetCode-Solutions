class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        def is_stretchy(word):
            i = 0
            j = 0

            while i < len(s) and j < len(word):
                if s[i] != word[j]:
                    return False

                char = s[i]

                count_s = 0
                while i < len(s) and s[i] == char:
                    count_s += 1
                    i += 1

                count_word = 0
                while j < len(word) and word[j] == char:
                    count_word += 1
                    j += 1

                if count_s < count_word:
                    return False

                if count_s != count_word and count_s < 3:
                    return False

            return i == len(s) and j == len(word)

        count = 0

        for word in words:
            if is_stretchy(word):
                count += 1

        return count