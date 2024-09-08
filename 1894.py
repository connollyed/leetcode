class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        k = k % total

        for idx,val in enumerate(chalk):
            k -= val
            if k < 0:
                #print(f"idx = {idx}")
                return idx
