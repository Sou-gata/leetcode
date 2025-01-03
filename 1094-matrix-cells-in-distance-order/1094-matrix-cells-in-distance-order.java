class Solution {
    public int[][] allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        int[][] matrix = new int[rows * cols][2];
        int k = 0;
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++){
                matrix[k][0] = i;
                matrix[k][1] = j;
                k++;
            }
            
        }
        Arrays.sort(matrix, new Comparator<int[]>() {
            public int compare(int a[], int b[]) {
                int A = Math.abs(a[0] - rCenter) + Math.abs(a[1] - cCenter);
                int B = Math.abs(b[0] - rCenter) + Math.abs(b[1] - cCenter);
                return A - B;
            }
        });
        return matrix;
    }
}