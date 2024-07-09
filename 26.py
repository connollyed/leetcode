class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        value = float('-inf')
        idx = 0
        for i in nums:
            if i > value:
                nums[idx] = i
                value = i
                idx += 1
        return idx
    

# IMPROVED SOLUTION


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:        
        l = 1
        
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
            return l
