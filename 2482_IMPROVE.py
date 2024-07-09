class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n_rows = len(grid[0])
        n_cols = len(grid)


        onesRow = []
        zeroRow = []
        for cur_row in range(n_cols):
            one_count = 0
            zero_count = 0

            for cur_col in range(n_rows):
                if grid[cur_row][cur_col] == 1:
                    one_count += 1
                else:
                    zero_count += 1

            onesRow.append(one_count)
            zeroRow.append(zero_count)


        onesCol = []
        zeroCol = []
        
        for cur_col in range(n_rows):
            one_count = 0
            zero_count = 0

            for cur_row in range(n_cols):
                if grid[cur_row][cur_col] == 1:
                    one_count += 1
                else:
                    zero_count += 1

            onesCol.append(one_count)
            zeroCol.append(zero_count)

         
        #print("----------")
        #print(onesRow)
        #print("----------")
        #print(onesCol)
        #print("----------")
        #print(zeroRow)
        #print("----------")
        #print(zeroCol)
        #print("----------")

        diff = []
        for i in range(n_cols):
            cur_diff = []
            for j in range(n_rows):
#                print(f"{i} and {j}")
                value = onesRow[i] + onesCol[j] - zeroRow[i] - zeroCol[j]
#                print(value)
                cur_diff.append(value)
            diff.append(cur_diff)


#        print(diff)
        return diff
#        row,col
#        [
#        [0,1,1]
#        [1,0,1]
#        [0,0,1]
#        ]