class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        while i < len(nums):
            
            
            print(f"{i} {nums[i]}")
            if nums[i] == val:
                nums.remove(val)
                i -= 1

            
            i += 1


        return len(nums)