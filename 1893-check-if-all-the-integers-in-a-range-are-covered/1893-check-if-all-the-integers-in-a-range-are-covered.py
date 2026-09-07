class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr = []

        for i in range(left, right+1):
            arr.append(i)

        c = 0
        for x in arr:
            for i in range(len(ranges)):
                if ranges[i][0] <= x <= ranges[i][1]:
                    c += 1
                    break
        return c == len(arr)