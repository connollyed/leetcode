class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        nums1 = set(nums1)
        nums2 = set(nums2)

        smallest = 10**9 + 1
        if len(nums1) < len(nums2):
            for i in nums1:
                if i in nums2:
                    smallest = min(smallest,i)

        else:
            for i in nums2:
                if i in nums1:
                    smallest = min(smallest,i)


        return -1 if smallest == (10**9 + 1) else smallest