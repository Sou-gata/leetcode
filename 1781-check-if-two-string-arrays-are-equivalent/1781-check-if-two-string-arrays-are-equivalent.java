class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        if (word1[0].charAt(0) != word2[0].charAt(0)) {
            return false;
        }
        String s1 = String.join("", word1);
        String s2 = String.join("", word2);
        return s1.equals(s2);
    }
}