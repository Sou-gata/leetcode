class Solution {
    public int maxWidthOfVerticalArea(int[][] points) {
        int l = points.length;
        int[] x = new int[l];
        for (int i = 0; i < l; i++) {
            x[i] = points[i][0];
        }
        Arrays.sort(x);
        int max = 0;
        for (int i = 1; i < l; i++) {
            int d = x[i] - x[i - 1];
            if (d > max) {
                max = d;
            }
        }
        return max;
    }
}