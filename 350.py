class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        f1 = Counter(nums1)
        f2 = Counter(nums2)

        union = []
        seen = set()
        for k1 in nums1:

            if k1 in seen:
                continue

            seen.add(k1)
            if k1 in f2:
                for i in range(min(f1[k1],f2[k1])):
                    union.append(k1)

        return union