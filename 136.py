class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        t = 0
        for i in nums:
            t = t ^ i

        return t