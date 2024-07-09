class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n_rows = len(board)
        n_cols = len(board[0])
        
        def dfs(r,c,idx,prev_r,prev_c):
            if r >= n_rows or r < 0:
                return False
            if c >= n_cols or c < 0:
                return False

            if (board[r][c] == word[idx]) and ((r,c) not in seen):
                seen.add((r,c))
                if idx+1 == len(word):
                    return True
            
                res = dfs(r+1,c,idx+1,r,c) or dfs(r-1,c,idx+1,r,c) or dfs(r,c+1,idx+1,r,c) or dfs(r,c-1,idx+1,r,c)
                seen.remove((r,c))
                return res
            return False

        seen = set()
        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == word[0]:    
                    if dfs(r,c,0,r,c) == True:
                        return True
                    
#                    if (dfs(r+1,c,1) or dfs(r-1,c,1) or dfs(r,c+1,1) or dfs(r,c-1,1)) == True:
#                        return True

        return False
    """
    ["A","B","C","E"]
    ["S","F","E","S"]
    ["A","D","E","E"]
    """