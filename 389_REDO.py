class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq_s = {}
        freq_t = {}

        for i in range(len(t)-1):
            if s[i] not in freq_s:
                freq_s[s[i]] = 1
            else:
                freq_s[s[i]] += 1
        

            if t[i] not in freq_t:
                freq_t[t[i]] = 1
            else:
                freq_t[t[i]] += 1
        
        if t[-1] not in freq_t:
            freq_t[t[-1]] = 1
        else:
            freq_t[t[-1]] += 1

        for i, (k, v) in enumerate(freq_t.items()):
            if (k not in freq_s):
                return k
            if (v != freq_s[k]):
                return k
        
        print(freq_s)


# I worked this out myself but I needed to debug it
# especially the middle part t[-1]