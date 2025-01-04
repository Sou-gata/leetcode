class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        int l = arr.length;
        int total = 0;
        for(int i = 0; i < l; i++){
            total += arr[i];
        }
        if(l % 2 == 1 && l != 1){
            total *= 2;
        }
        for(int windowSize = 3; windowSize <= l; windowSize += 2){
            if(windowSize == l && l % 2 == 1) {
                break;
            }
            int prefixSum = 0;
            for(int i = 0; i < windowSize; i++){
                prefixSum += arr[i];
            }
            total += prefixSum;
            for(int i = 1; i <= l - windowSize; i++){
                prefixSum += (arr[i + windowSize - 1] - arr[i - 1]);
                total += prefixSum;
            }
        }
        return total;
    }
}