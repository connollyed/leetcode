class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(list(allowed))

        count = 0
        for word in words:
            w = list(word)
            valid = True
            for i in w:
                if i not in allowed:
                    valid = False
                    break
            
            if valid:
                count += 1
                
        return count
