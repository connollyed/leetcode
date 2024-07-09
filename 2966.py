class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        
        ret_val = []
        current = []
        ptr_3 = 1
        i = 0
        
        while(i < len(nums)):
            current.append(nums[i])

            if(ptr_3 == 3):
                ret_val.append(current)
                print(current)
                if (abs(current[0] - current[-1]) > k):
                    return []
                
                current = []
                ptr_3 = 0


            ptr_3 += 1
            i += 1

        return ret_val