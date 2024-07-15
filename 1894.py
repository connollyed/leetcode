class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        n = len(chalk)
        idx = 0

        total_used_per_round = sum(chalk)

        k = k % total_used_per_round

        while k > 0:
            k -= chalk[idx]
            idx = (idx + 1) % n

            print(k)

        if k == 0:
            return idx
        else:
            if idx == 0:
                return n - 1

            return idx - 1