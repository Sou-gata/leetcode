class Solution {
    private int[][] rotate(int[][] mat){
        int n = mat.length;
        int[][] res = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                res[n - j - 1][i] = mat[i][j];
            }
        }
        return res;
    }
    private boolean isEqual(int[][] mat, int[][] target){
        int n = mat.length;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(mat[i][j] != target[i][j]){
                    return false;
                }
            }
        }
        return true;
    }
    private void printMatrix(int[][] mat){
        for(int i = 0; i < mat.length; i++){
            System.out.println(Arrays.toString(mat[i]));
        }
    }
    public boolean findRotation(int[][] mat, int[][] target) {
        if(isEqual(mat, target)){
            return true;
        }
        int[][] t = rotate(mat);
        for(int i = 0; i < 3; i++){
            if(isEqual(t, target)){
                return true;
            }
            if(i != 2){
                t = rotate(t);
            }
        }
        return false;
    }
}