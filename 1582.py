class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        max_y = len(mat)
        max_x = len(mat[0])

        special = 0

        r = 0
        c = 0

        cur_x = 0
        cur_y = 0
        for cur_x in range(0,max_x):
            for cur_y in range(0,max_y):

                if mat[cur_y][cur_x] == 0:
                    continue
                hasOne = 1

                # right left
                #print("GOING RIGHT")
                for j in range(0,max_x):
                    #print(f"{cur_y},{j} = {mat[cur_y][j]}")
                    if mat[cur_y][j] == 1 and j != cur_x:
                        hasOne += 1
            
                # up down
                #print("GOING DOWN")
                for j in range(0,max_y):
                    #print(f"{j},{cur_x} = {mat[j][cur_x]}")
                    if mat[j][cur_x] == 1 and j != cur_y:
                        hasOne += 1


                if hasOne == 1:
                    special += 1

                #print(f"special = {special}")

        return special


# Cant scan along diagonaals because of edge case below

#[0,0,0,0,0]
#[1,0,0,0,0]
#[0,1,0,0,0]
#[0,0,1,0,0]
#[0,0,0,1,1]