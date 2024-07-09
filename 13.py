class Solution:
    def romanToInt(self, s: str) -> int:

        conversion = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }

        output = 0 

        i = len(s) - 1
        while ( i >= 0 ):

            cur = s[i]

            if( i-1 >= 0) :
                
                prev = s[i-1]

                if (( cur == "X" or cur == "V") and prev == "I"):
                    output += conversion[cur] - 1
                    i -= 1

                elif (( cur == "L" or cur == "C") and prev == "X"):
                    output += conversion[cur] - 10
                    i -= 1

                elif(( cur == "D" or cur == "M") and prev == "C"):
                    output += conversion[cur] - 100
                    i -= 1
                
                else:
                    output += conversion[cur]
                
               
            else:
                output += conversion[cur]
            
            i -= 1

        return output


sol = Solution()
print(sol.romanToInt("III"))
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("MCMXCIV"))









#
class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }

        res = 0 

        for i in range(len(s)):
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res