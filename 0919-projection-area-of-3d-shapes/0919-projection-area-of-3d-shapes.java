class Solution {
    public int projectionArea(int[][] grid) {
        int n = grid.length;
        int xy = 0, xz = 0, yz = 0;
        for(int i = 0; i < n; i++) {
            int max = grid[i][0];
            for(int j = 0; j < n; j++){
                if(grid[i][j] > 0){
                    xy++;
                }
                if(grid[i][j] > max){
                    max = grid[i][j];
                }
            }
            xz += max;
        }
        for(int i = 0; i < n; i++) {
            int max = grid[0][i];
            for(int j = 0; j < n; j++) {
                if(grid[j][i] > max) {
                    max = grid[j][i];
                }
            }
            yz += max;
        }
        return xy + xz + yz;
    }
}