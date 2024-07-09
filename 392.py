class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        count = 0
        for i in s:
            while ptr < len(t):
                while i != t[ptr] and ptr < len(t)-1:
                    ptr += 1

                if i == t[ptr]:
                    count += 1
                    ptr += 1
                    break

                ptr += 1

        return count == len(s)