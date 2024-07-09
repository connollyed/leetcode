class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        total_lasers = []
        for r in bank:
            print(r)
            lasers = 0
            cur_row = r
            for c in range(len(cur_row)):
                if cur_row[c] == "1":
                    lasers += 1

            if lasers > 0:
                total_lasers.append(lasers)

        res = 0
        for idx in range(1, len(total_lasers)):
            res = res + (total_lasers[idx] * total_lasers[idx - 1])

        return res