class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = 0
        middle = len(nums)//2
        y = middle

        res = []
        while x < middle and y < len(nums):
            res.append(nums[x])
            res.append(nums[y])

            x+=1
            y+=1

        return res