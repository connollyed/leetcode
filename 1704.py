class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        str1 = s[0:len(s)//2]
        str2 = s[len(s)//2:len(s)]

        #print(str1)
        #print(str2)

        str1_vowels = 0
        for i in str1:
            if i in vowels:
                str1_vowels += 1


        str2_vowels = 0
        for i in str2:
            if i in vowels:
                str2_vowels += 1


        return str1_vowels == str2_vowels