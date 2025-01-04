class Solution {
    public int[] frequencySort(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            if (map.containsKey(num)) {
                map.put(num, map.get(num) + 1);
            } else {
                map.put(num, 1);
            }
        }
        int[][] mapArr = new int[map.size()][2];
        int[] ans = new int[nums.length];
        int k = 0;
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            mapArr[k][0] = entry.getKey();
            mapArr[k][1] = entry.getValue();
            k++;
        }
        Arrays.sort(mapArr, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return (a[1] * 300 + (300 - a[0])) - (b[1] * 300 + (300 - b[0]));
            }
        });
        k = 0;
        for (int[] ints : mapArr) {
            for (int j = 0; j < ints[1]; j++) {
                ans[k] = ints[0];
                k++;
            }
        }
        return ans;
    }
}