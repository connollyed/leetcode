class Solution:
    def maxScore(self, s: str) -> int:
        
        max_total = 0
        for m in range(1,len(s)):
            
            zero_count = 0
            ones_count = 0
            for l in range(m):
                #count 0
                if s[l] == "0":
                    zero_count += 1
            for r in range(m,len(s)):
                #count 1
                if s[r] == "1":
                    ones_count += 1

            total = zero_count + ones_count

            max_total = max(max_total, total)

        return max_total