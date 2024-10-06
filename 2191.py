class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        conversions = []

        for i,n in enumerate(nums):
            decimal_value_convert = 0
            pos = 0
            if n == 0:
                decimal_value_convert = mapping[0]
            else:
                while n > 0:
                    digit = n % 10
                    n = n // 10

                    decimal_value_convert += (mapping[digit] * 10**pos)
                    pos += 1

            # map of decimal values
            conversions.append((decimal_value_convert,i))

        conversions.sort()
        print("sort", conversions)

        output = []
        for val,i in conversions:
            output.append(nums[i])

        return output
