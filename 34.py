class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) - 1
        L = 0
        R = n

        while(L<=R):
            mid = (L + R) // 2

            #print(nums[mid])

            if (nums[mid] == target):
                #print("FOUND")
                target_L = mid
                target_R = mid
                
                while(target_L >= 0 and nums[target_L] == target):
                    target_L -= 1


                while(target_R <= n and nums[target_R] == target):
                    target_R += 1

                
                return [target_L+1,target_R-1]

            elif(nums[mid] < target):
                #print("TARGET IS BIGGER")
                L = mid + 1

            else:
                #print("TARGET IS SMALLER")
                R = mid - 1
        
        return [-1,-1]