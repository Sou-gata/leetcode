class Solution {
    public int maximumDifference(int[] nums) {
        int prefixMin = nums[0], maxDiff = -1, d;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == prefixMin) {
                continue;
            }
            d = nums[i] - prefixMin;
            if (d > maxDiff) {
                maxDiff = d;
            }
            if (nums[i] < prefixMin) {
                prefixMin = nums[i];
            }
        }
        return maxDiff;
    }
}