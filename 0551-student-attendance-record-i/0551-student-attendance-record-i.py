class Solution:
    def checkRecord(self, s: str) -> bool:
        a_count = 0
        l_stric = 0

        for c in s:
            if c == 'A':
                a_count += 1
                if a_count >= 2:
                    return False
            
            if c == 'L':
                l_stric += 1
                if l_stric >= 3:
                    return False
            else:
                l_stric = 0
        return True