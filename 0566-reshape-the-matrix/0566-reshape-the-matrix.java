class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int row = mat.length;
        int col = mat[0].length;
        if(r * c != row * col){
            return mat;
        }
        int[][] reshaped = new int[r][c];
        int[] flatMat = new int[r * c];
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                flatMat[(i * col) + j] = mat[i][j];
            }
        }
        int colIdx = 0;
        int rowIdx = 0;
        for(int i = 0; i < flatMat.length; i++){
            reshaped[rowIdx][colIdx] = flatMat[i];
            colIdx++;
            if(colIdx == c){
                colIdx = 0;
                rowIdx++;
            }
        }
        return reshaped;
    }
}