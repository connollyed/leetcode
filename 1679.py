class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        #print(nums)
        
        L, R = 0, len(nums) - 1
        count = 0

        while L < R:
            sum = nums[L] + nums[R]
            if(sum == k):
                count += 1
                L += 1
                R -= 1
            elif(sum < k):
                L += 1
            else:
                R -= 1

        return count