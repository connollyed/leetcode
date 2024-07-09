class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        seen = set()
        def search(r,c, cur_gold, max_gold):

            if (r,c) in seen or r<0 or c<0 or r>=n_row or c>=n_col or grid[r][c]==0:
                return max_gold
            
            seen.add((r,c))
            cur_gold += grid[r][c]

            max_gold = max(max_gold, cur_gold)

            #print(f"{r},{c}, value = {grid[r][c]}, cur = {cur_gold} and max = {max_gold}")

            max_gold = max(max_gold,search(r+1,c, cur_gold,max_gold))
            max_gold = max(max_gold,search(r-1,c, cur_gold,max_gold))
            max_gold = max(max_gold,search(r,c+1, cur_gold,max_gold))
            max_gold = max(max_gold,search(r,c-1, cur_gold,max_gold))

            seen.remove((r,c))
            return max_gold




        n_row = len(grid)
        n_col = len(grid[0])

        
        max_gold = 0
        for r in range(n_row):
            for c in range(n_col):
                if grid[r][c] != 0:
                    max_gold = max(max_gold,search(r,c,0,max_gold))
        
        return max_gold