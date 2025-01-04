class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        Arrays.sort(boxTypes, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return b[1] - a[1];
            }
        });
        int t = truckSize, sum = 0;
        for (int[] boxType : boxTypes) {
            int boxNumber = boxType[0];
            if (t - boxNumber >= 0) {
                t -= boxNumber;
                sum += boxNumber * boxType[1];
            } else if (t < boxNumber) {
                sum += t * boxType[1];
                break;
            }
        }
        return sum;
    }
}