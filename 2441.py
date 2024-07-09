class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        biggest = 0
        table = set()
        for i in nums:
            if -i in table:
                biggest = max(biggest,i,-i)
            table.add(i) 

        if biggest == 0:
            return -1

        return biggest