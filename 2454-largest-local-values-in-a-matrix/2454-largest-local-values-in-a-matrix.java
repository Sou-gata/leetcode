class Solution {
    public int[][] largestLocal(int[][] grid) {
        int n = grid.length;
        int[][] ansMat = new int[n - 2][n - 2];
        for(int i = 0; i < n - 2; i++){
            for(int j = 0; j < n - 2; j++){
                int[] arr = {grid[i][j], grid[i][j + 1], grid[i][j + 2], grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2], grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]};
                int max = arr[0];
                for(int k = 1; k < arr.length; k++){
                    if(arr[k] > max){
                        max = arr[k];
                    }
                }
                ansMat[i][j] = max;
            }
        }
        return ansMat;
    }
}