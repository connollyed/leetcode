class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ("a","e","i","o","u")

        count = 0
        max_count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        #    print(s[i])
        
        #print(f"{s[i]} and {count}")
        #print(i)

        max_count = max(max_count,count)

        for i in range(1, len(s) - k + 1) :
            #print(f"{i}, {k} to {i+k}")
            if s[i-1] in vowels:        # off by one here
                count -= 1
            if s[i+k-1] in vowels:      # off by one here
                count += 1
            #print(f"{s[i-1]} to {s[i+k-1]}, count = {count}")
            #print(f"final {s[i+k]}")
            max_count = max(max_count,count)


        return max_count
        #   0   1   2   3   4   5   6   7   8   9   10  11
        #   w   e   a   l   l   l   o   v   e   y   o   u

        #   t   r   y   h   a   r   d
        #       L               R                   k    =  4

        #   a   b   c   i   i   i   d   e   f