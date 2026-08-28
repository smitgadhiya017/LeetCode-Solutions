class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        set1 = list(set(nums))
        set1.sort(reverse = True)
        ans = []
        for i in range(k):
            if i == len(set1):
                break
            ans.append(set1[i])
        return ans