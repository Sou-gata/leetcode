class Solution {
    public boolean divideArray(int[] nums) {
        int counts[] = new int[501];
        for (int i = 0; i < nums.length; i++) {
            counts[nums[i]]++;
        }
        for (int count : counts) {
            if (count % 2 != 0) {
                return false;
            }
        }
        return true; 
    }
}