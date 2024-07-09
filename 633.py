class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        R = ceil(sqrt(c))
        L = 0
        while L <= R:
            sum = L**2 + R**2
            if sum == c:
                return True
            elif sum < c:
                L+=1
            elif sum > c:
                R-=1
        
        return False
    
x = Solution()
x.judgeSquareSum(60)
print(hi)
