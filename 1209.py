class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []  # Letter, count
        for i in s:
            
            if len(stack) == 0 or i != stack[-1][0]:
                stack.append([i,1])
            else:
                letter, count = stack.pop(-1)
                if count+1 != k:
                    stack.append([letter, count+1])

            #print(stack)

        output = ""
        for letter,count in stack:
            output += letter*count
        return output