class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        exp = sorted(heights)

        for i in range(len(exp)):
            if heights[i] != exp[i]:
                count += 1

        return count