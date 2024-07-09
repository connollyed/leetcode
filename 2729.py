# O(n) time and O(n) space

class Solution:
    def isFascinating(self, n: int) -> bool:
        n2 = n * 2
        n3 = n * 3

        str_val = str(n) + str(n2) + str(n3)

        freq_counter = set()
        for i in str_val:
            if i in freq_counter or i == '0':
                return False
            else:# i not in freq_counter:
                freq_counter.add(i)

        if len(freq_counter) == 9:
            return True
        else:
            return False
