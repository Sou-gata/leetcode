class Solution {
    public String firstPalindrome(String[] words) {
        for (int i = 0; i < words.length; i++) {
            int len = words[i].length();
            boolean isPalindrom = true;
            for(int j = 0; j < len / 2; j++){
                if(words[i].charAt(j) != words[i].charAt(len - 1 - j)){
                    isPalindrom = false;
                    break;
                }
            }
            if(isPalindrom) {
                return words[i];
            }
        }
        return "";
    }
}