class Solution:
    def climbStairs(self, n: int) -> int:

        #res = []

        @cache
        def solve(n):
            if n == 1:
                return 1
            if n == 2:
                return 2

            return solve(n-1) + solve(n-2)

        return solve(n)
        


# MANUAL MEMO
class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        #@cache
        def solve(n):
            if n == 1:
                return 1
            if n == 2:
                return 2

            if n not in memo:
                memo[n] = solve(n-1) + solve(n-2)

            return memo[n]

        return solve(n)
        