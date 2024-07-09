class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n_row = len(land)
        n_col = len(land[0])

        ret_val = []
        def bfs(r,c, min_r,min_c, max_r, max_c):
            land[r][c] = 0

            min_r = min(min_r,r)
            min_c = min(min_c,c)
            max_r = max(max_r,r)
            max_c = max(max_c,c)

            if (r-1) >= 0 and land[r-1][c] == 1:
                min_r, min_c, max_r, max_c = bfs(r-1, c, min_r, min_c, max_r, max_c)
                min_r = min(min_r,r)
                min_c = min(min_c,c)
                max_r = max(max_r,r)
                max_c = max(max_c,c)


            if (r+1) < n_row and land[r+1][c] == 1:
                min_r, min_c, max_r, max_c = bfs(r+1, c, min_r, min_c, max_r, max_c)
                min_r = min(min_r,r)
                min_c = min(min_c,c)
                max_r = max(max_r,r)
                max_c = max(max_c,c)
            
            if (c-1) >= 0 and land[r][c-1] == 1:
                min_r, min_c, max_r, max_c = bfs(r, c-1, min_r, min_c, max_r, max_c)
                min_r = min(min_r,r)
                min_c = min(min_c,c)
                max_r = max(max_r,r)
                max_c = max(max_c,c)
            
            if (c+1) < n_col and land[r][c+1] == 1:
                min_r, min_c, max_r, max_c = bfs(r, c+1, min_r, min_c, max_r, max_c)
                min_r = min(min_r,r)
                min_c = min(min_c,c)
                max_r = max(max_r,r)
                max_c = max(max_c,c)

            return min_r, min_c, max_r, max_c

        for r in range(n_row):
            for c in range(n_col):
                if land[r][c] == 1:
                    min_r, min_c, max_r, max_c = r, c, r, c
                    min_r, min_c, max_r, max_c = bfs(r, c, r, c, r, c)
                    ret_val.append([min_r,min_c,max_r,max_c])


        return ret_val