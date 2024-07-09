class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        dests = []
        src = []
        for i in paths:
            s,d = i

            src.append(s)
            dests.append(d)

        for j in dests:
            if j not in src:
                return j