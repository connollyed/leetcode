class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        
        res = []        
        for i in range(0,n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            L = i + 1
            R = n - 1
            
            while L < R:
                sum = nums[i] + nums[L] + nums[R]

                if sum == 0:
                    res.append([nums[i], nums[L], nums[R]])

                    # Skip duplicates for left and right pointers
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1

                    L += 1
                    R -= 1
                    
                elif sum > 0:
                    R -= 1
                else:
                    L += 1
            
        return res