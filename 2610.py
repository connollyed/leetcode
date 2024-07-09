class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        while len(nums) > 0:
            # 1 Pass of nums creating a row
            used = set()
            cur_row =  []
            for i in reversed(nums):
                if i not in used:
                    cur_row.append(i)
                    used.add(i)
                    nums.remove(i)
            res.append(cur_row)

        return res

# come at arrat from end so we dont lose our position
    
"""
my_list = [1, 2, 3, 4, 5]
elements_to_keep = []

for element in my_list:
    if not condition_to_remove_element:
        elements_to_keep.append(element)

# Reassign the original list with the filtered elements
my_list = elements_to_keep
"""