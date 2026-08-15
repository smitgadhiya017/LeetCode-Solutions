class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxi1 = max(nums)
        maxi2 = float("-inf")
        maxi3 = float("-inf")

        for i in nums:
            if i != maxi1:
                maxi2 = max(maxi2, i)
    
        if maxi2 == float("-inf"):
            return maxi1

        for i in nums:
            if i != maxi1 and i != maxi2:
                maxi3 = max(maxi3, i)
        
        if maxi3 == float("-inf"):
            return maxi1
            
        return maxi3

        