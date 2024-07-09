class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        intersection = []
        for i in nums1:
            if (i in nums2):
                intersection.append(i)

        return intersection
    
#   O(n*m) time complexity
#   O(n+m) space complexity