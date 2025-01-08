class Solution {
    private boolean isPrefixAndSuffix(String str1, String str2) {
        if (str1 == null || str2 == null) {
            return false;
        }
        return str2.startsWith(str1) && str2.endsWith(str1);
    }

    public int countPrefixSuffixPairs(String[] words) {
        int count = 0;
        for (int i = 0; i < words.length; i++) {
            for (int j = 0; j < words.length; j++) {
                if (i >= j) continue;
                if (isPrefixAndSuffix(words[i], words[j])) {
                    count++;
                }
            }
        }
        return count;
    }
}