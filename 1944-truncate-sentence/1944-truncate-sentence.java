class Solution {
    public String truncateSentence(String s, int k) {
        String[] words = s.split(" ");
        StringBuilder str = new StringBuilder(words[0] + (k != 1 ? " " : ""));
        for(int i = 1; i < k; i++){
            str.append(words[i]+ (i != k - 1 ? " " : "" ));
        }
        return str.toString();
    }
}