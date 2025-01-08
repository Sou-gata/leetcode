class Solution {
    public int countElements(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int min = nums[0];
        int max = nums[0];
        for (int num : nums) {
            if (map.containsKey(num)) {
                map.put(num, map.get(num) + 1);
            } else {
                map.put(num, 1);
            }
            if (num < min) {
                min = num;
            }
            if (num > max) {
                max = num;
            }
        }
        if (min == max) {
            return 0;
        }
        return nums.length - map.get(min) - map.get(max);
    }
}