class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        l = 0
        r = len(s)-1

        s = list(s)
        while l < r:
            
            while s[l] not in vowels and l < r:
                l+=1
            
            while s[r] not in vowels and l < r:
                r-=1


            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
        
        return "".join(s)