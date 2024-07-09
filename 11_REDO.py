class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1

        max_area = 0
        while L < R:
            cur_area = (R-L) * min(height[L],height[R]) 
            max_area = max(max_area, cur_area)

            if height[L] > height[R]:
                R -= 1
            else:
                # THIS IS CONDITION 
                # height[L] <= height[R]
                L += 1

        return max_area
    