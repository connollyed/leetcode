class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def bfs(r,c):
            cur_area = 0
            queue = []
            queue.append((r,c))
           
            while len(queue) > 0:
                r,c = queue.pop(0)

                if r >= 0 and r < max_y and c >= 0 and c < max_x:

                    if(grid[r][c] == 1):
                        print(f"{r}, {c}")
                        cur_area += 1
                        grid[r][c] = 0
                        
                        queue.append((r+1,c))
                        queue.append((r-1,c))
                        queue.append((r,c+1))
                        queue.append((r,c-1))

            return(cur_area)




        max_x = len(grid[0])
        max_y = len(grid)



        max_area = 0
        for r in range(max_y):
            for c in range(max_x):
                if grid[r][c] == 1:
                    max_area = max(max_area,bfs(r,c))

        return max_area


        