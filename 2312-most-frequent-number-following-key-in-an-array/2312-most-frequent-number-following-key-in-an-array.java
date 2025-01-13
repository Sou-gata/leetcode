class Solution {
    public int mostFrequent(int[] nums, int key) {
        HashMap<Integer, Integer> counts = new HashMap<>();
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == key) {
                if (counts.containsKey(nums[i + 1])) {
                    counts.put(nums[i + 1], counts.get(nums[i + 1]) + 1);
                } else {
                    counts.put(nums[i + 1], 1);
                }
            }
        }
        int max = 0, e = 0;
        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            if (entry.getValue() > max) {
                max = entry.getValue();
                e = entry.getKey();
            }
        }
        return e;
    }
}