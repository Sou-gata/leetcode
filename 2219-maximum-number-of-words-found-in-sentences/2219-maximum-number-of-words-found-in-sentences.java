class Solution {
    public int mostWordsFound(String[] sentences) {
        int max = 0;
        for(String s : sentences) {
            int word = s.split(" ").length;
            if (word > max) {
                max = word;
            }
        }
        return max;
    }
}