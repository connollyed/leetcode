class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        found = False
        for idx,val in enumerate(word):
            stack.insert(0,val)
            if val == ch:
                found = True
                break
        
        if found:
            ret = "".join(stack)
            print(ret)
            ret += word[idx+1:]
            return ret
        else:
            return word