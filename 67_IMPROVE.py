class Solution:
    def addBinary(self, a: str, b: str) -> str:

        if a is None and b is None:
            return ""
        if a is None:
            return b
        if b is None:
            return a

        a = a[::-1]
        b = b[::-1]

        #print(f"a = {a}")
        #print(f"b = {b}")

        sum = ""
        c = 0

        cur = 0
        while cur < len(a) and cur < len(b):
            a_i = int(a[cur])
            b_i = int(b[cur])

            s = a_i ^ b_i ^ c
            c = a_i & b_i | ((a_i ^ b_i) & c)

            print(f"c {c}")

            sum += str(s)
            cur += 1

        while cur < len(a):
            sum += str(int(a[cur]) ^ c)
            c = int(a[cur]) & c
            cur += 1

        while cur < len(b):
            sum += str(int(b[cur]) ^ c)
            c = int(b[cur]) & c
            cur += 1

        if c != 0:
            sum += str(c)
        return sum[::-1]