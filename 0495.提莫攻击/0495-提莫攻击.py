class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        return 0 if len(timeSeries) == 0 else sum([min(duration, timeSeries[i+1] - timeSeries[i])
                                                  for i in range(len(timeSeries)-1)] + [duration])
        """
        ret = 0
        for i in range(len(timeSeries)-1):
            ret += min(duration, timeSeries[i+1] - timeSeries[i])
        if len(timeSeries) > 0:
            ret += duration
        
        return ret
        """