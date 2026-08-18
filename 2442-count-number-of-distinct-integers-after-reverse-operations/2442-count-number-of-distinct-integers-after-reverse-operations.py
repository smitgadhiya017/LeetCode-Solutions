class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])

        for i in range(len(nums)):
            temp = nums[i]
            rev = 0
            while temp:
                d = temp % 10
                rev = rev * 10 + d
                temp //= 10
            
            ans.append(rev)
     
        set1 = set()
        for i in range(len(ans)):
            set1.add(ans[i])

        return len(set1)