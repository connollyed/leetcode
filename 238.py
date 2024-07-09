class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * (len(nums) + 1)
        for idx,val in enumerate(nums):
            prefix[idx] = val * prefix[idx-1]
        #prefix.pop(-1)


        postfix = [1] *(len(nums) + 1)
        for idx in range (len(nums) - 1, 0-1, -1):
            postfix[idx] = nums[idx] * postfix[idx+1]
        #postfix.pop(0)

        #print(prefix)
        #print(postfix)

        mul = [0] * len(nums)
        for i in range(0,len(nums)):
            mul[i] = prefix[i-1] * postfix[i+1]

        return mul