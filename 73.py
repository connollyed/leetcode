class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        max_x = len(matrix[0])
        max_y = len(matrix)

        loc = set() # locations of zeros
        for r in range(max_y):
            for c in range(max_x):
                if (matrix[r][c] == 0):
                    loc.add((r,c))

        for i in loc:
            x,y = i

            for c in range(max_x):
                matrix[x][c] = 0
            for r in range(max_y):
                matrix[r][y] = 0

    
# naive solution 
# time: O(n*m) and space: 0(n*m)
# copy matrix, and go through original setting
# the copies rows,columns to 0

# timecomplexity O(n*m) and space complexity O(n+m)
# have 2 arrays one fol cols one for rows
# scan through matrix if 0 set, value appropriate values
# in row and column array

#