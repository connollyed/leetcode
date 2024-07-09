class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        max_x = len(matrix[0])
        max_y = len(matrix)

        x =  max_x - 1
        y =  0

        while True:
            current_element = matrix[y][x]
            
            if target == current_element:
                return True
            
            elif target < current_element:
                x -= 1
                if x<0 or x >= max_x:
                    return False

            elif target > current_element:
                y += 1
                if y<0 or y >= max_y:
                    return False

            else:
                return False
                