class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        int mat[][] = new int[m][n];
        if(m * n != original.length){
            return new int[0][0];
        }
        int rowIdx = 0, colIdx = 0;
        for(int i = 0; i < original.length; i++){
            mat[rowIdx][colIdx] = original[i];
            colIdx++;
            if(colIdx == n){
                colIdx = 0;
                rowIdx++;
            }
        }
        return mat;
    }
}