class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        str1 = ""

        for i in digits:
            str1 += str(i)

        total = int(str1) + 1

        return list(map(int, str(total)))