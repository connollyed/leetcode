class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        position = 1
        direction = 1
        while time > 0:
            time -= 1

            if direction == 1:
                position += 1
            else:
                position -= 1 

            if position == n or position == 1:
                direction *= -1
        return position