class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        
        l = 1
        r = 7

        t = 0

        cur = 1
        l = 1

        while True:
            cur = l
            while cur <= r:
                total += cur
                cur += 1
                t += 1

                if t >= n:
                    return total

            l += 1
            r += 1