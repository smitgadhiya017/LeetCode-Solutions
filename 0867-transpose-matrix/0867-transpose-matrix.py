class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r = len(matrix)
        c = len(matrix[0])
        ans = [[0] * r for _ in range(c)]
    
        c1 = 0
        for i in range(r): 
            r1 = 0
            for j in range(c):
                ans[r1][c1] = matrix[i][j]
                r1 += 1
            c1 += 1
        return ans
       
