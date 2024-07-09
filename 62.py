class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        print(m,n)
        arr = [[0 for i in range(m)] for j in range(n)]
        
        for r in range(n):
            arr[r][0] = 1

        for c in range(m):
            arr[0][c] = 1

        for r in range(1,n):
            for c in range(1,m):
                arr[r][c] = arr[r-1][c] + arr[r][c-1]
        #print(arr)

        return arr[n-1][m-1]
    
# Can be improved