class Solution {
    public List<Integer> twoOutOfThree(int[] nums1, int[] nums2, int[] nums3) {
        HashSet<Integer> s1 = new HashSet<>(), s2 = new HashSet<>(), s3 = new HashSet<>(), s = new HashSet<>(), result = new HashSet<>();
        for (int i : nums1) {
            s1.add(i);
            s.add(i);
        }
        for (int i : nums2) {
            s2.add(i);
            s.add(i);
        }
        for (int i : nums3) {
            s3.add(i);
            s.add(i);
        }
        for (int i : s) {
            if ((s1.contains(i) && s2.contains(i)) || (s2.contains(i) && s3.contains(i)) || (s3.contains(i) && s1.contains(i))) {
                result.add(i);
            }
        }
        return new ArrayList<>(result);
    }
}