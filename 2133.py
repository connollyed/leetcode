class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        N = len(matrix)
        print(f"num of rows: {N}")
        
        seen = set()
        for r in range(N):
            seen.clear()
            for c in range(N):
                if matrix[r][c] in seen:
                    #print(f"{matrix[r][c]} for col")
                    return False

                seen.add(matrix[r][c])
                
        for c in range(N):
            seen.clear()
            for r in range(N):
                if matrix[r][c] in seen:
                    #print(f"{matrix[r][c]} for row")
                    return False

                seen.add(matrix[r][c])

        return True