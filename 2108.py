class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        def isPalindrome(word):
            L = 0
            R = len(word) - 1

            while L < R:
                if word[L] != word[R]:
                    return False
                L += 1
                R -= 1

            return True

        for w in words:
            if (isPalindrome(w) == True):
                return w
        
        return ""

# O(1) Space
# O(n*m) Time, where n is number of words and m is average word length