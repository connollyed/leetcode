class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        max_x = len(matrix[0])
        max_y = len(matrix)
        
        x = max_x - 1
        y = 0


        while x>=0 and y < max_y :
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] > target:
                x -= 1
            else:
                y += 1
        
        return False
        
#    [1,4,7,11,15]
#    [2,5,8,12,19]
#    [3,6,9,16,22]
#    [10,13,14,17,24]
#    [18,21,23,26,30]