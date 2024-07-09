class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            notfound = False
            for j in range(len(needle)):

                print(f"{i} + {j} = {i+j}")

                if (i+j) >= len(haystack):
                    notfound = True
                    break
                    
                if haystack[i+j] != needle[j]:
                    notfound = True
                    break
            
            if notfound == False:
                return i

        return -1

sol = Solution()
print(sol.strStr("mississippi", "issipi"))