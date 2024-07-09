class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
    
        output = []
        for i in nums:
            digits = []

            while i > 0:
                current = i % 10
                i = i // 10

                digits.insert(0,current)
            print(digits)
            for k in digits:
                output.append(k)

        return output
    







    # 2nd Solution
    class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
    
        output = []
        for i in nums:
            for j in str(i):
                output.append(int(j))

        return output