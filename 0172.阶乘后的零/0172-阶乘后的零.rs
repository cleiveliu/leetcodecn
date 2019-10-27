impl Solution {
    pub fn trailing_zeroes(n: i32) -> i32 {
        let mut ret = 0;
        let mut n = n;
        while n > 0 {
            ret += n/5;
            n /= 5
        }
        return ret;
    }
}