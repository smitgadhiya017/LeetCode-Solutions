class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        maxi = 3000
        ans = []
        for i in range(1,maxi):
            if i not in arr:
                ans.append(i)
        
        for i in range(len(ans)):
            if i+1 == k:
                return ans[i]

