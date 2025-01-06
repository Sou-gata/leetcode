class Solution {
    public int timeRequiredToBuy(int[] tickets, int k) {
        int time = 0;
        if(tickets[k] == 1) {
            return k + 1;
        }
        for(int i = 0; i < tickets.length; i++) {
            if(i <= k) {
                time += Math.min(tickets[i], tickets[k]);
            } else {
                time += Math.max(1, Math.min(tickets[i], tickets[k] - 1));
            }
        }
        return time;
    }
}