class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        xor_prefix = [0 for i in range(n)]

        xor_prefix[0] = arr[0] 

        #print(n,xor_prefix)
        for i in range(1,n):
            xor_prefix[i] = arr[i] ^ xor_prefix[i-1]

        output = []
        for s,e in queries:
            if s == 0:
                res = xor_prefix[e]
            else:
                res = xor_prefix[e] ^ xor_prefix[s-1]
            output.append(res)

        return output