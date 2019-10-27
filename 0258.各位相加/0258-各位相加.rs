impl Solution {
    pub fn add_digits(n: i32) -> i32 {
        if n < 10 { n } else { Self::add_digits( n%10 + Self::add_digits(n/10))}
    }
}