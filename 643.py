class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg =  float('-inf')
        
        total = 0
        for i in range(0,k):
            total += nums[i]
        max_avg = max(total/k, max_avg)

        for ptr in range(0,len(nums)-k):
            total = total - nums[ptr] + nums[ptr + k]
            max_avg = max(total/k, max_avg)

        return max_avg