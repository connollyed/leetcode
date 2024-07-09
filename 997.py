class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        pos_judge = [i for i in range(1,n+1)]
        #print(pos_judge)

        for a,b in trust:
            #print(f"{a},{b}")
            if a in pos_judge:
                pos_judge.remove(a)
            #print(pos_judge)

        if len(pos_judge) == 1:

            judge = pos_judge.pop(0)
            
            trusts_judge = []
            for a,b in trust:
                if b == judge:
                    trusts_judge.append(b)

            if len(trusts_judge) == n-1:
                return judge

        return -1