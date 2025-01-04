class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        int invalid = 0;
        for (String word : words) {
            for (int j = 0; j < word.length(); j++) {
                if (allowed.indexOf(word.charAt(j)) < 0) {
                    invalid++;
                    break;
                }
            }
        }
        return words.length - invalid;
    }
}