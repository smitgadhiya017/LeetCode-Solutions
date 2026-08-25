class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = []
        for i in nums1:
            c = 0
            for j in nums2:
                if i != j:
                    c += 1
            
            if c == len(nums2):
                if i not in ans1:
                    ans1.append(i)

        ans2 = []
        for i in nums2:
            c = 0
            for j in nums1:
                if i != j:
                    c += 1
            
            if c == len(nums1):
                if i not in ans2:
                    ans2.append(i)
        
        return [ans1,ans2]
