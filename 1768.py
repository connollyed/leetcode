# time complexity O(n) or O(m) which ever string is bigger
# space complexity O(n+m)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ret_val = ""

        i = 0
        while i < len(word1) and i < len(word2):
            ret_val += (word1[i] + word2[i])
            i += 1

        if i < len(word1):
            ret_val += word1[i:]
        else:
            ret_val += word2[i:]

        return ret_val