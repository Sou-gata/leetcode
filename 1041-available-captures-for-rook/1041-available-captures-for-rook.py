class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_pos = [-1, -1]
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    rook_pos = [i, j]
                    break
        count = 0
        # check up
        for i in range(rook_pos[0] - 1, -1, -1):
            if board[i][rook_pos[1]] == "p":
                count += 1
                break
            elif board[i][rook_pos[1]] == "B":
                break
        # check down
        for i in range(rook_pos[0] + 1, 8):
            if board[i][rook_pos[1]] == "p":
                count += 1
                break
            elif board[i][rook_pos[1]] == "B":
                break
        # check left
        for i in range(rook_pos[1] - 1, -1, -1):
            if board[rook_pos[0]][i] == "p":
                count += 1
                break
            elif board[rook_pos[0]][i] == "B":
                break
        # check right
        for i in range(rook_pos[1] + 1, 8):
            if board[rook_pos[0]][i] == "p":
                count += 1
                break
            elif board[rook_pos[0]][i] == "B":
                break
        return count