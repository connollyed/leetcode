class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) <= 4:
            return 0
        
        smallest = sorted(heapq.nsmallest(4,nums))
        biggest  = sorted(heapq.nlargest(4,nums))

        return abs(min(biggest[0] - smallest[0], biggest[1] - smallest[1], biggest[2] - smallest[2], biggest[3] - smallest[3]))