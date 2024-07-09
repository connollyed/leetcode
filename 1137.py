class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def helper(n):
            if n in memo:
                return memo[n]

            if n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            else:
                result = helper(n-1) + helper(n-2) + helper(n-3)
                memo[n] = result
                return result

        
        return helper(n)
    
# sol 2
    class Solution:
    
    cache = {}
    def tribonacci(self, n: int) -> int:
        if n in self.cache.keys():
            return self.cache[n]
        
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        self.cache[n] = (self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1))
        return self.cache[n]
