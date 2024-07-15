class Solution:
    result = 0
    def maximumGain(self, s: str, x: int, y: int) -> int:
        

        def search(needle,val,s):
            stack = [""]
            n = len(s)
            top = ""

            i = 0
            while i < n:
                top = stack[-1]
                
                if top + s[i]  == needle:
                    self.result += val
                    stack.pop(-1)
                else:
                    stack.append(s[i])

                i += 1
            
            print(stack)

            return "".join(stack)
        if x > y:
            string=search("ab",x,s)
            search("ba",y,string)
        else:
            string = search("ba",y,s)
            string = search("ab",x,string)
        
        return self.result