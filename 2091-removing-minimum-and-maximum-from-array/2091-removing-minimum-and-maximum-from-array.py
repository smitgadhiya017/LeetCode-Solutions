class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mini = min(nums)
        maxi = max(nums)
        c1 = 1
        c2 = 1
        for i in range(len(nums)):
            if mini != nums[i]:
                c1 += 1
            else:
                break
        for i in range(len(nums)):
            if maxi != nums[i]:
                c2 += 1
            else:
                break
        ans1 = max(c1,c2) 

        c3 = 1
        c4 = 1
        for i in range(len(nums)-1,-1,-1):
            if mini != nums[i]:
                c3 += 1
            else:
                break
        for i in range(len(nums)-1,-1,-1):
            if maxi != nums[i]:
                c4 += 1
            else:
                break
        
        ans2 = max(c3,c4)

        ans3 = min(c1+c4, c2+c3)

        return min(ans1,ans2,ans3)
        

            