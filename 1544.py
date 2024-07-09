class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for i in s:
            if len(stack) != 0:
                # lower == upper
                if (ord(stack[-1]) ^ (ord(i))) == 32 :
                    stack.pop(-1)
                else:
                    stack.append(i)
            else:
                stack.append(i)

        return "".join(stack)
