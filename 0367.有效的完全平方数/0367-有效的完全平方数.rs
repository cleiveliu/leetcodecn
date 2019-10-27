impl Solution {
    pub fn is_perfect_square(num: i32) -> bool {
        (0u64..).filter(|x| x*x >= num as u64)
                .map(|x| x*x)
                .nth(0) == Some(num as u64)          
    }
}