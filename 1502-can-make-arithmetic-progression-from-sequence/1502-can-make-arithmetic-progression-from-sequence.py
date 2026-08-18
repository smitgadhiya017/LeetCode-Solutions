class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        ans = []
        total = 0
        for i in range(1,len(arr)):
            total = arr[i] - arr[i-1]
            ans.append(total)

        for i in range(len(ans)-1):
            if ans[i] != ans[i+1]:
                return False
        return True