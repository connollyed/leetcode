class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == ")" :
                if len(stack) > 0:
                    top = stack[-1]
                    if top == "(":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            elif i == "]" :
                if len(stack) > 0:
                    top = stack[-1]
                    if top == "[":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            elif i == "}":
                if len(stack) > 0:
                    top = stack[-1]
                    if top == "{":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(i)

        if len(stack) == 0:
             return True