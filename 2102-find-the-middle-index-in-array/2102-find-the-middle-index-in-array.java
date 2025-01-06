class Solution {
    public int findMiddleIndex(int[] nums) {
        int n = nums.length, rightSum = 0, leftSum = 0;
        for (int num : nums) {
            rightSum += num;
        }
        for (int i = 0; i < n; i++) {
            if (rightSum - nums[i] == leftSum) {
                return i;
            }
            rightSum -= nums[i];
            leftSum += nums[i];
        }
        return -1;
    }
}