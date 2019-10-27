impl Solution {
    pub fn max_area(xs: Vec<i32>) -> i32 {
        let mut i = 0;
        let mut j = xs.len()-1;
        let mut ret = 0;
        while i < j {
            ret = ret.max(xs[i].min(xs[j]) * ((j-i) as i32));
            if xs[i] < xs[j] {
                i += 1;
            } else {
                j -= 1;
            }
        }
        
        ret
    }
}