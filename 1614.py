class Solution:
    def maxDepth(self, s: str) -> int:
        b = 0
        depth = 0 
        for i in s:
            if i == "(":
                b += 1
                pass
            elif i == ")":
                b -=1

            depth = max(depth, b)

        return depth