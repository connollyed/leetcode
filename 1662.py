class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        

        word1_str = ""
        for i in word1:
            word1_str += i

        word2_str = ""
        for i in word2:
            word2_str += i

        if (word1_str) == (word2_str):
            return True
        else:
            return False


