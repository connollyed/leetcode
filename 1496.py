class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = []

        cur = [0, 0]
        visited.append(cur[:])
        
        for i in path:
            if i == "N":
                cur[0] = cur [0] + 1
            elif i == "S":
                cur[0] = cur [0] - 1
            elif i == "E":
                cur[1] = cur [1] + 1
            else: #i == "W":
                cur[1] = cur [1] - 1

            print(f"dir = {i}")
            print(f"cur = {cur}")
            print(f"visited = {visited}")
            if cur in visited:
                return True
            
            visited.append(cur[:])
        
        return False

# Tuple Version
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()  # Use a set to store visited positions

        cur = (0, 0)
        visited.add(cur)

        for i in path:
            if i == "N":
                cur = (cur[0] + 1, cur[1])
            elif i == "S":
                cur = (cur[0] - 1, cur[1])
            elif i == "E":
                cur = (cur[0], cur[1] + 1)
            else:  # i == "W":
                cur = (cur[0], cur[1] - 1)

            if cur in visited:
                return True
            else:
                visited.add(cur)

        return False
