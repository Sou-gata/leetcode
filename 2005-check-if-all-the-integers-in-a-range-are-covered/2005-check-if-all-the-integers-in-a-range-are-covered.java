class Solution {
    public boolean isCovered(int[][] ranges, int left, int right) {
        boolean covered = true;
        for (int i = left; i <= right; i++) {
            boolean c = false;
            for (int[] range : ranges) {
                if (range[0] <= i && i <= range[1]) {
                    c = true;
                    break;
                }
            }
            covered = c && covered;
        }
        return covered;
    }
}