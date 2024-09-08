class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        max_dist = 0
        obs_dict = set()
        for x,y in obstacles:
            obs_dict.add((x,y))

        x,y = 0,0
        dir = [(0,1),(1,0),(0,-1),(-1,0)] # N E W S
        dir_idx = 0
        for k in commands:
            if k == -2:
                dir_idx -= 1
                if dir_idx<0:
                    dir_idx = 3
            elif k == -1:
                dir_idx += 1
                dir_idx = dir_idx % 4
            else:
                go_x,go_y = dir[dir_idx]
                for i in range(k):               
                    x += go_x
                    y += go_y

                    print(x,y)
                    if ((x,y)) in obs_dict:
                        #print("hit obs")
                        x -= go_x
                        y -= go_y
                        break

                    max_dist = max(max_dist, x**2 + y**2)

        return max_dist