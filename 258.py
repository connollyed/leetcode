class Solution:
    def addDigits(self, num: int) -> int:
        
        while(num >= 10):
            num_list = list(str(num))
            num = 0
            for i in num_list:
                num += int(i)
            
        return num