class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        words = s.split(" ")
        print(words)

        for i in reversed(words):
            if i != "":
                return len(i)
        
        return 0
    

# improve solution have ptr at end
# loop while = " " when not != start counting
# stop when you reach a == " "