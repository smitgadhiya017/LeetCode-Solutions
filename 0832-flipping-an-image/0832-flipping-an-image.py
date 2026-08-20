class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        r = len(image)
        c = len(image[0])
        ans = [[0] * c for _ in range(r)]
        r1 = 0
        for i in range(r):
            c1 = len(image)-1
            for j in range(c):
                ans[r1][c1] = image[i][j]
                c1 -= 1
            r1 += 1

        for i in range(r):
            for j in range(c):
                if ans[i][j] == 0:
                    ans[i][j] = 1
                else:
                    ans[i][j] = 0
        return ans 
