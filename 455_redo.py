class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        child = 0
        cookie = 0
        count = 0
        while cookie < len(s) and child < len(g):
            if s[cookie] >= g[child]:
                count += 1
                child += 1
        
            cookie += 1
        return count