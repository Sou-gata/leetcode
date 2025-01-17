class Solution {
    public int minimumOperations(int[] nums) {
        boolean[] counts = new boolean[101];
        for(int i = 0; i < nums.length; i++) {
            counts[nums[i]] = true;
        }
        int opr = 0;
        for (int i = 1; i < counts.length; i++) {
            if (counts[i]) {
                opr++;
            }
        }
        return opr;
    }
}