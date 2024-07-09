class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        L = 0
        R = 0
        total = 0

        size = float('inf')
        while R < len(nums):
            total += nums[R]
            print(f"total = {total} L={L} and R={R}")
            while total >= target:
                size = min(size, R-L+1)
                total -= nums[L]
                L += 1
            R+=1
                
            #print(f"L={L} and R={R}")

        if size == float('inf'):
            return 0
        else:
            return size