class Solution {
    public double trimMean(int[] arr) {
        int removeLen = arr.length / 20;
        Arrays.sort(arr);
        double sum = 0.0;
        for(int i = removeLen; i < arr.length - removeLen; i++){
            sum += arr[i];
        }
        double mean = sum / (arr.length - 2 * removeLen);
        return mean;
    }
}