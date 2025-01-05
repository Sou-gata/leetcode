class Solution {
    public int maximumPopulation(int[][] logs) {
        int[] years = new int[101];
        for(int[] log : logs) {
            for(int i = log[0] - 1950; i < log[1] - 1950; i++) {
                years[i]++;
            }
        }
        int max = Arrays.stream(years).max().getAsInt();
        for (int i = 0; i < years.length; i++) {
            if(years[i] == max){
                return i + 1950;
            }
        }
        return 0;
    }
}