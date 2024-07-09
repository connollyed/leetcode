# O(n) time and O(1) space
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        biggest = 0
        biggest2nd = 0

        for i in nums:
            if i >= biggest:
                biggest2nd = biggest
                biggest = i
            elif i > biggest2nd:
                biggest2nd = i

        return (biggest - 1) * (biggest2nd-1) 


# O(nlogn) time and O(n) spance
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sorted_num = sorted(nums)
        return (sorted_num[-1]-1) * (sorted_num[-2]-1)
    