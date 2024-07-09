class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        max_x = len(grid)
        max_y = len(grid[0])

        print(f"{max_x} {max_y}")        

        max_val = max_x * max_y

        repeated = float('-inf')
        freq = set()
        for r in range(0,max_y):
            for c in range(0,max_x):
                print(grid[r][c])
                if grid[r][c] not in freq:
                    freq.add(grid[r][c])
                else:
                    repeated = grid[r][c]

        print(freq)

        not_present = float('-inf')
        for i in range(max_val+1):
            if i not in freq:
                not_present = i

        
        return [repeated, not_present]