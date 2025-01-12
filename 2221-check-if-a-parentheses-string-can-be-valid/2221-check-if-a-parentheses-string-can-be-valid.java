class Solution {
    public boolean canBeValid(String s, String locked) {
        int n = s.length();
        if (n % 2 != 0) {
            return false;
        }
        int openMin = 0, openMax = 0;
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            char lock = locked.charAt(i);
            if (lock == '1') {
                if (ch == '(') {
                    openMin++;
                    openMax++;
                } else {
                    openMin--;
                    openMax--;
                }
            } else {
                openMin--;
                openMax++;
            }
            openMin = Math.max(openMin, 0);
            if (openMax < 0) {
                return false;
            }
        }
        int closeMin = 0, closeMax = 0;
        for (int i = n - 1; i >= 0; i--) {
            char ch = s.charAt(i);
            char lock = locked.charAt(i);

            if (lock == '1') {
                if (ch == ')') {
                    closeMin++;
                    closeMax++;
                } else {
                    closeMin--;
                    closeMax--;
                }
            } else {
                closeMin--;
                closeMax++;
            }
            closeMin = Math.max(closeMin, 0);
            if (closeMax < 0) {
                return false;
            }
        }
        return openMin == 0 && closeMin == 0;
    }
}