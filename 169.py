class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)

        print(nums)

        cur_count = 1
        cur_number = nums[0]
        for i in range(1,len(nums)):
            print(i)
            if nums[i] > cur_number:
                cur_number = nums[i]
                cur_count = 1
            else:
                cur_count += 1

                if(cur_count > (len(nums)//2)):
                    return cur_number
        
        return cur_number
    

# Improved Solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        freq_map = {}
        for i in nums:
            val = freq_map.get(i, 0) + 1
            if val > floor(n / 2):
                return i
            freq_map[i] = val