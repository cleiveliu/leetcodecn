impl Solution {
    pub fn is_power_of_three(n: i32) -> bool {
        let n: i64 = n as i64;
        for i in 0.. {
            if n == 3_i64.pow(i as u32) {
                return true;
            }
            if 3_i64.pow(i as u32) > n {
                return false;
            }
        }
        return false;
    }
}