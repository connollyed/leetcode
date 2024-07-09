class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        L = 0
        longest = 0
        seen = {}
        for idx, val in enumerate(s):
            #print(val)
            if val not in seen:
                #print(f"ADD {val}")
                seen[val] = idx
                #print(f"idx - L = {idx}-{L} and longest = {longest}")
                longest = max(longest, idx - L + 1)
            else:
                while val in seen:
                    #print("------BEFORE")
                    #print(seen)
                    #print(f"REMOVE {val}")
                    #print(f"S[L] = {s[L]} and L={L}")
                    del seen[s[L]]
                    #print(seen)               
                    L += 1
                seen[val] = idx
        
        return longest