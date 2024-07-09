class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        longest = 0
        val = 0

        cnt = Counter(s)
        values = [i for i in cnt.values()]
        values.sort(reverse=True)
        
        for i in values:
            if i % 2 == 0:
                longest += i
            else:
                longest += (i - 1)
                val = 1

            
        return longest + val