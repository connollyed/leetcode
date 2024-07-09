class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = []

        if x < 0:
            return False

        while x > 0:
            digits.append(int(x % 10))
            x = x // 10

        #print(digits)

        i = 0
        while i < len(digits)/2:
        #    print(f"{digits[i]}:{digits[len(digits)-1-i]}")
            if digits[i] != digits[len(digits)-1-i]:
                return False
            i+=1

        return True