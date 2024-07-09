class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        max_y = len(grid)
        max_x = len(grid[0]) if max_y > 0 else 0
        perimeter = 0

        def dfs(x, y):
            nonlocal perimeter

            if x < 0 or x >= max_x or y < 0 or y >= max_y or grid[y][x] == 0:
                perimeter += 1
                return

            if grid[y][x] == -1:  # Visited
                return

            grid[y][x] = -1  # Mark cell as visited

            dfs(x - 1, y)  # left
            dfs(x + 1, y)  # right
            dfs(x, y - 1)  # down
            dfs(x, y + 1)  # up

        for y in range(max_y):
            for x in range(max_x):
                if grid[y][x] == 1:
                    dfs(x, y)
                    return perimeter  # Return perimeter after the first island is processed

        return perimeter  # Return perimeter if grid doesn't contain any island
