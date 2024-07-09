class Solution:
    def minOperations(self, s: str) -> int:
        start_one = []
        start_zero = []
        for i in range(0,len(s)):
            if i % 2 == 0:
                start_one.append(1)
                start_zero.append(0)
            else:
                start_one.append(0)
                start_zero.append(1)
            

        s = list(s)
        count_one = 0
        count_zero = 0
        for i in range(0,len(s)):
            print(i)
            if int(s[i]) != start_one[i]:
                count_one += 1

            if int(s[i]) != start_zero[i]:
                count_zero += 1

        return min(count_one,count_zero)