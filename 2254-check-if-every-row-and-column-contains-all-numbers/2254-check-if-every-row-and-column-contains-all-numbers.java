class Solution {
    public boolean checkValid(int[][] matrix) {
        HashSet<Integer> set;
        for (int[] row : matrix) {
            set = new HashSet<>();
            for (int j : row) {
                set.add(j);
            }
            if (set.size() != matrix.length) {
                return false;
            }
        }
        for (int i = 0; i < matrix.length; i++) {
            set = new HashSet<>();
            for (int j = 0; j < matrix.length; j++) {
                set.add(matrix[j][i]);
            }
            if (set.size() != matrix.length) {
                return false;
            }
        }
        return true;
    }
}