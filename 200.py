class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        NUM_R = len(grid)
        NUM_C = len(grid[0])

        count = 0

        def bfs(r,c):
            #print(grid)
            #print(f"cur:{r} {c} {NUM_R} {NUM_C}")
            if r>=NUM_R or r<0 or c<0 or c>=NUM_C or grid[r][c]!="1":
                return

            grid[r][c] = "0"
            
            bfs(r+1,c)
            bfs(r-1,c)
            bfs(r,c+1)
            bfs(r,c-1)

                
        print(f"{NUM_R} {NUM_C}")
        for r in range(NUM_R):
            for c in range(NUM_C):
                if grid[r][c] == "1":
                    #print(f"{r}, {c}")
                    count += 1
                    bfs(r,c)

        #for i in range(NUM_R):
        #    print(grid[i])
        return count