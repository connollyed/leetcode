class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == None or len(nums) == 0:
            return 0

        nums.sort()
        prev = nums[0]

        max_count = 0
        count = 1
        
        i = 1
        while i < len(nums):
            if (prev == nums[i]-1):
                prev = nums[i]
                count += 1
                i += 1
            elif prev == nums[i]:
                i+=1
                continue
            else:
                prev = nums[i]
                max_count = max(max_count,count)
                count = 1
                i+=1

        max_count = max(max_count,count)
        return max_count