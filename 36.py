class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N_ROW = len(board)
        N_COL = len(board[0])

        seen = set()
        for r in range(N_ROW):
            seen.clear()
            for c in range(N_COL):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    #print(f"ROW: {board[r][c]}")
                    return False
                seen.add(board[r][c])

        for c in range(N_COL):
            seen.clear()
            for r in range(N_COL):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    #print(f"COL {board[r][c]}")
                    return False
                seen.add(board[r][c])


        for i in range(3):
            for j in range(3):
                # NEW SQUARE
                seen.clear()
                for r in range(3):
                    for c in range(3):
                        cur_r = r+(i*3)
                        cur_c = c+(j*3)

                        if board[cur_r][cur_c] == ".":
                            continue

                        if board[cur_r][cur_c] in seen:
                            #print(seen)
                            #print(f"SQUARE {board[cur_r][cur_c]}")
                            return False
                        seen.add(board[cur_r][cur_c])

        return True