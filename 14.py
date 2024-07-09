class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longest = strs[0]

        i = 1
        while i < len(strs):
            
            # compare longest to strs[0] and update longest
            compare = strs[i]

            j = 0
            while j < len(longest) and j < len(compare):
                if longest[j] != compare[j]:
                    break
                j+=1

            longest = longest[0:j]
            i += 1

        return longest