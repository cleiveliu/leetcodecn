func findPoisonedDuration(timeSeries []int, duration int) int {
    ret := 0
    i := 0
    for i < len(timeSeries) - 1 {
        ret += min(duration, timeSeries[i+1]-timeSeries[i])
        i += 1
    }
    if len(timeSeries) > 0 {
        ret += duration
    }
    
    return ret
 }

func min(a, b int) int {
    if a < b {
        return a
    } else {
        return b
    }
}
