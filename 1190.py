class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        i = 0
        while i < len(s): 
            cur = s[i]
            if cur == ")":
                # begin popping
                rev = []

                while stack[-1] != "(":
                    rev.append(stack.pop(-1))

                stack.pop(-1)
                stack += rev
            else:
                stack.append(cur)
                #print(f"APP,{stack}")
            i+=1

        #print(stack)
        return "".join(stack)