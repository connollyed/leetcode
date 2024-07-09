class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = -1
        missing = -1

        seen = set()
        for i in range(len(nums)):
            cur = nums[i]
            if cur in seen:
                duplicate = cur
            seen.add(cur)

        for i in range(1,len(nums)+1):
            if i not in seen:
                missing = i
                break  

        return [duplicate, missing]
