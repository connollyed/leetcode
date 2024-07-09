class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        s_ptr = 0
        t_ptr = 0

        n_t = len(t)
        n_s = len(s)
        while s_ptr < n_s and t_ptr < n_t:
            if s[s_ptr] == t[t_ptr]:
                t_ptr += 1
            
            s_ptr += 1

        
        return n_t - t_ptr