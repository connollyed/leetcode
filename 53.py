class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = -10**4
        total = 0
        for i in nums:
            total += i
            max_sum = max(max_sum, total)
            
            if total < 0:
                total = 0

        return max_sum