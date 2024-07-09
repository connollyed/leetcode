class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_alpha = ""
        for i in list(s):
            if i.isalpha():
                s_alpha += i.lower()

        print(s_alpha)

        j = len(s_alpha)-1
        i = 0
        while i <= j:
            if s_alpha[i] != s_alpha[j]:
                return False
            i += 1
            j -= 1

        return True