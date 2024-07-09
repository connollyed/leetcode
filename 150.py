class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = ["+","-","/","*"]
        for i in tokens:
            #print(stack)
            if i not in ops:
                stack.append(int(i))
            else:
                var2 = stack.pop(-1)
                var1 = stack.pop(-1)
                if i == "+":
                    stack.append(var1 + var2)
            
                elif i == "-":
                    stack.append(var1 - var2)

                elif i == "/":
                    stack.append(int(var1 / var2))
                    #print(stack[-1])

                elif i == "*":
                    stack.append(var1 * var2)

        #print(stack)
        return stack[0]