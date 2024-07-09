class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        table = {}
        for index, i in enumerate(nums):
            print(table)
            find = target - i
            print(f"{find}, {i}")
            if i not in table:
                table[find] = index
            else:
                ret_val = []
                ret_val.append(table[i])
                ret_val.append(index)
                return ret_val

sol = Solution()
sol.twoSum([2,7,11,15], 9)