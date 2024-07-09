class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        n_open = 0
        n_close = 0

        stack = []
        res = []
        def gen(n_open, n_close):
            
            # BASE CASE - Found a valid one
            if n_open == n_close == n:
                res.append( "".join(stack) )
                return
            
            if n_open < n:
                stack.append("(")
                gen(n_open + 1, n_close)
                stack.pop()

            if n_open > n_close:
                stack.append(")")
                gen(n_open, n_close + 1)
                stack.pop()

        gen(n_open, n_close)
        return res