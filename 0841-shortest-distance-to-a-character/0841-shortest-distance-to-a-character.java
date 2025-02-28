class Solution {
    public int[] shortestToChar(String s, char c) {
        int lastIndex = s.length();
        int[] distances = new int[s.length()];
        for (int i = 0; i < distances.length; i++) {
            if (s.charAt(i) != c) {
                if (lastIndex != distances.length) {
                    distances[i] = Math.abs(lastIndex - i);
                } else {
                    distances[i] = distances.length;
                }
            } else {
                lastIndex = i;
            }
        }
        lastIndex = distances.length;
        for (int i = distances.length - 1; i >= 0; i--) {
            if (s.charAt(i) != c) {
                if (lastIndex != distances.length) {
                    distances[i] = Math.min(Math.abs(lastIndex - i), distances[i]);
                }
            } else {
                lastIndex = i;
            }
        }
        return distances;
    }
}