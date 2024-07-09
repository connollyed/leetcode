class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def binarysearch(nums,target,l,r):

            while l <= r:
                mid = (l + r)//2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
                
            return l

        return binarysearch(nums,target,0,len(nums)-1)
