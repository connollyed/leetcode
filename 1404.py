class Solution:
    def numSteps(self, s: str) -> int:
        val = int(s,2)
        #print(val)
        count = 0
        while val > 1:
            if val % 2 == 0:
                val = val >> 1
            else:
                val += 1
            
            count += 1
        
        return count