class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        result = []
        def helper(n_left,n_right):

            #print(n_left,n_right)
            if n_left == n_right == n:
                #print(result)
                result.append("".join(stack))
                return
            
            if n_left < n:
                stack.append("(")
                helper(n_left + 1, n_right)
                #n_left -= 1
                stack.pop()

            if n_left > n_right:
                stack.append(")")
                helper(n_left, n_right + 1)
                #n_right-=1
                stack.pop()

        
        helper(0,0)
        return result