class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0

        while n > 0:
            bit = n % 2
            n = n // 2

            if bit == 1:
                count += 1

        return count

# ises n & n-1