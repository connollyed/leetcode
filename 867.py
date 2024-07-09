class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        new_array = [[0 for i in range(n_rows)] for j in range (n_cols)]

        for i in range(0,n_cols):
            for j in range(0,n_rows):
                new_array[i][j] = matrix[j][i]

        return new_array