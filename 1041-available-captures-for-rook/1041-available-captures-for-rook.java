class Solution {
    public int numRookCaptures(char[][] board) {
        int[] rookPos = {-1, -1};
        for(int i = 0; i < 8; i++) {
            for(int j = 0; j < 8; j++) {
                if (board[i][j] == 'R') {
                    rookPos[0] = i;
                    rookPos[1] = j;
                }
            }
        }
        int count = 0;
        // check up
        for(int i = rookPos[0] - 1; i >= 0; i--){
            if(board[i][rookPos[1]] == 'p') {
                count++;
                break;
            } else if(board[i][rookPos[1]] == 'B') {
                break;
            }
        }
        // check down
        for(int i = rookPos[0] + 1; i < 8; i++) {
            if(board[i][rookPos[1]] == 'p') {
                count++;
                break;
            } else if(board[i][rookPos[1]] == 'B') {
                break;
            }
        }
        // check left
        for(int i = rookPos[1] -1; i >= 0; i--) {
            if(board[rookPos[0]][i] == 'p'){
                count++;
                break;
            } else if(board[rookPos[0]][i] == 'B') {
                break;
            }
        }
        // check right
        for(int i = rookPos[1] + 1; i < 8; i++) {
            if(board[rookPos[0]][i] == 'p'){
                count++;
                break;
            } else if(board[rookPos[0]][i] == 'B') {
                break;
            }
        }
        return count;
    }
}