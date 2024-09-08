class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        # m = rows
        # n = cols

        if m*n != len(original):
            return []

        mat = [ [0 for i in range(n)] for j in range(m) ]
        print(mat)

        for idx,val in enumerate(original):
            c = idx % n
            r = idx // n
            mat[r][c] = val 

        return mat