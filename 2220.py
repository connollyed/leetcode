class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        num = start^goal

        count = 0
        while num > 0:
            bit = num & 1
            if bit == 1:
                count += 1
            num = num >> 1 

        return count