class Solution:
    def countBits(self, n: int) -> List[int]:
    
        def toBinary(num):
            bits = []
            while num > 0:
                bits.append(num % 2)
                num = num // 2

            return bits

        def countOnes(bits_list):
            count = 0
            for i in bits_list:
                if i == 1:
                    count += 1

            return count


        res = []
        for i in range(0, n+1):
            bits_list = toBinary(i)
            n_ones = countOnes(bits_list)
            res.append(n_ones)

        print(res)
        return res
