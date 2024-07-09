class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)

        freq = {}
        for i in words:
            for s in i:
                if s in freq:
                    freq[s] += 1
                else:
                    freq[s] = 1

        for i,(k,v) in enumerate(freq.items()):
            if v % n != 0:
                return False
        
        return True

    # CAN DO WITH ARRAY