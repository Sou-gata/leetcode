class Solution {
    public int maxDistance(int[] colors) {
        int idx1 = 0, idx2 = colors.length - 1;
        for (int i = colors.length - 1; i >= 1; i--) {
            if (colors[i] != colors[idx1]) {
                idx1 = i;
                break;
            }
        }
        for (int i = 0; i < colors.length - 1; i++) {
            if (colors[i] != colors[idx2]) {
                idx2 = i;
                break;
            }
        }
        return Math.max(idx1, colors.length - idx2 - 1);
    }
}