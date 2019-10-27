impl Solution {
    pub fn my_pow(x: f64, n: i32) -> f64 {
        fn h(x: f64, n: i64) -> f64 {
            if n == 0{
                return 1.0;
            }
            if n & 1 == 0 {
                return h(x,n/2) * h(x, n/2);
            } else {
                return x * h(x,n-1);
            }
        }
        let n = n as i64;
        if n > 0 { h(x,n) } else { 1.0/h(x,-n) }
    }
}