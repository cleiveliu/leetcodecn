impl Solution {
    pub fn hamming_distance(x: i32, y: i32) -> i32 {
        let mut ret = 0;
        let mut n = x ^ y;
        while n > 0 {
            if n & 1 == 1 {
                ret += 1;
            }
            n = n >> 1;
        }
        
        
        ret
    }
}