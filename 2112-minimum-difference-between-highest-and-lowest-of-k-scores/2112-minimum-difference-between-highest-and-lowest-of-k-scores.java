class Solution {
    public int minimumDifference(int[] nums, int k) {
        Arrays.sort(nums);
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length - k + 1; i++) {
            int d = nums[i + k - 1] - nums[i];
            if (d < min) {
                min = d;
            }
        }
        return min;
    }
}