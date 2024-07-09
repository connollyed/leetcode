class Solution:
    def reverse(self, x: int) -> int:
        minus = False
        
        if x < 0:
            minus = True

        x = abs(x)

        digits = []
        while x > 0:
            cur_digit = x % 10
            #print(cur_digit)
            digits.append(cur_digit)
            x = x // 10

        #print(digits)
        ret_val = 0
        for i in digits:
            ret_val *= 10
            ret_val += i

        if ((ret_val > (2**31 - 1)) or (ret_val < -2**31)):
            return 0

        if minus:
            return -1*ret_val
        
        return ret_val

