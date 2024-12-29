class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) < 5:
            return "Pending"
        board = []
        for i in range(3):
            board.append(['.'] * 3)
        for i in range(len(moves)):
            cell = moves[i]
            if i % 2 == 0:
                board[cell[0]][cell[1]] = 'A'
            else:
                board[cell[0]][cell[1]] = 'B'

        for i in range(3):
            # check rows
            t = board[i][0]
            match = True
            for j in range(1, 3):
                if t == ".":
                    match = False
                    break
                if board[i][j] != t:
                    match = False
                    break
            if match:
                return t
            # check column
            match = True
            t = board[0][i]
            for j in range(1, 3):
                if t == ".":
                    match = False
                    break
                if board[j][i] != t:
                    match = False
                    break
            if match:
                return t
        if board[0][0] != "." and (board[0][0] == board[1][1] == board[2][2]):
            return board[0][0]
        if board[0][2] != "." and (board[0][2] == board[1][1] == board[2][0]):
            return board[0][2]
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"