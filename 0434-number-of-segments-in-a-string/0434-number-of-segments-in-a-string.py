class Solution:
   def countSegments(self, s: str) -> int:
    c = 0
    prev = " "

    for i in range(len(s)):
        if s[i] != " " and prev == " ":
            c += 1

        prev = s[i]

    return c