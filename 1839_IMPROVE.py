class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = list("aeiou")

        prev_vowel = ""
        ptr = 0
        
        max_count = 0
        count = 0
        for i in list(word):
            
            if i == "a" and prev_vowel != "a":
                prev_vowel = i
                count = 1
                ptr = 1

            elif i == vowels[ptr]:    #valid
                prev_vowel = i
                count += 1

                if ptr < len(vowels):
                    ptr += 1
                if ptr == len(vowels):
                    max_count = max(max_count,count)
                    ptr = 4
                
            elif i == prev_vowel:   #valid
                count += 1
            else:                   #invalid, reset
                ptr = 0
                count = 0
                prev_vowel = i

            

            #print(f"cur={i} ptr={ptr} and count={count} max={max_count}")
            
        return max_count

