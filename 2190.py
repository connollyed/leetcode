class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        
        table = defaultdict(int)
        for idx,val in enumerate(nums):
            if len(nums) - 1 == idx:
                break
            if val == key:
                table[nums[idx+1]]+=1

        output = -1
        cur_max = 0
        for k,f in table.items():
            if f > cur_max:
                output = k
                cur_max = f
        
        return output