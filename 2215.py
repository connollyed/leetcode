class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        unique1 = set()
        for i in nums1:
            if i not in nums2:
                unique1.add(i)

        unique2 = set()
        for i in nums2:
            if i not in nums1:
                unique2.add(i)

        return [list(unique1),list(unique2)]