class Solution {
    public char slowestKey(int[] releaseTimes, String keysPressed) {
        int longest = releaseTimes[0];
        int key = (int) keysPressed.charAt(0);
        for(int i = 1; i < releaseTimes.length; i++) {
            int press = releaseTimes[i] - releaseTimes[i - 1];
            int ascii = (int) keysPressed.charAt(i);
            if(press > longest || (press == longest && ascii > key)){
                longest = press;
                key = ascii;
            }
        }
        return (char)key;
    }
}