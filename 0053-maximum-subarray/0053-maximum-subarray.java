class Solution {
    public int maxSubArray(int[] nums) {
        int sum = 0;
        int maxSum = 0;
        int max = nums[0];
        for (int num : nums) {
            sum += num;
            if (sum < 0) sum = 0;
            if (sum > maxSum) maxSum = sum;
            if (num > max) max = num;
        }
        if (sum == 0 && max <= 0) {
            return max;
        } else {
            return maxSum;
        }
    }
}