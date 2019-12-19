impl Solution {
    pub fn find_poisoned_duration(time_series: Vec<i32>, duration: i32) -> i32 {
        if time_series.len() == 0 {
            return 0;
        }
        let mut ret = 0;
        let mut i: usize = 0;
        while i < time_series.len() - 1 {
            ret += (time_series[i+1] - time_series[i]).min( duration );
            i += 1;
        }
        if time_series.len() > 0 {
            ret += duration;
        }
        
        return ret;
    }
}