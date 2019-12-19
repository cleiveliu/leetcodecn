class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        int ret = 0;
        int i = 0;
        while (i < timeSeries.length - 1) {
            ret += Math.min(duration, timeSeries[i+1] - timeSeries[i]);
            i += 1;
        }
        if (timeSeries.length > 0) {
            ret += duration;
        }
        
        return ret;
    }
}