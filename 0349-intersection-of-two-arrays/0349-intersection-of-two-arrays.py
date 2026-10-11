class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst1 = list(set(nums1))
        lst2 = list(set(nums2))

        ans = []

        for i in range(len(lst1)):
            for j in range(len(lst2)):
                if lst1[i] == lst2[j]:
                    ans.append(lst1[i])
        return ans