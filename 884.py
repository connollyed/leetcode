class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = Counter(s1.split(" "))
        s2 = Counter(s2.split(" "))

        ret_val = []
        for k,v in s1.items():
            if k not in s2 and v == 1:
                ret_val.append(k)

        for k,v in s2.items():
            if k not in s1 and v == 1:
                ret_val.append(k)


        return ret_val