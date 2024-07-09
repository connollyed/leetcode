class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)

        heap = []
        for k,v in freq.items():
            heappush(heap, (-v,k))

        res = [""] * len(s)
        pos = 0
        while len(heap):
            v,k = heappop(heap)
            v = -v
            
            print(k,v)
            while v > 0:
                if res[pos] != "":
                    return ""

                res[pos] = k
                pos = (pos + 2) % len(s)
                if pos == 0:
                    pos = 1

                v -= 1
            print(res)

        res = "".join(res)
        for i in range(1,len(res)):
            if res[i-1] == res[i]:
                return ""
        return res