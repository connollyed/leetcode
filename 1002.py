class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        freq = Counter(words[0])
        for w in words:
            cur = Counter(w)
            
            for f in freq:
                freq[f] = min(freq[f], cur[f])


        res = []
        for k in freq:
            for cnt in range(freq[k]):
                res.append(k)

        return res