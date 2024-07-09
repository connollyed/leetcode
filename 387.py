class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        stack = []
        freq = {}
        for i in s:
            stack.append(i)
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        for idx,val in enumerate(stack):
            if freq[val] == 1:
                return idx
        
        return -1