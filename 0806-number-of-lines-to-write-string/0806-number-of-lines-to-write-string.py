class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        curWid = 0
        for ch in s:
            w = widths[ord(ch) - ord('a')]
            if curWid + w > 100:
                lines += 1
                curWid = w
            else:
                curWid += w
        return [lines, curWid]
            