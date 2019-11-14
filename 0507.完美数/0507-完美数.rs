impl Solution {
    pub fn check_perfect_number(num: i32) -> bool {
        let nums = vec![6, 28, 496, 8128, 33550336];
        for &n in nums.iter() {
            if n == num {
                return true;
            }
        }
        return false;
    }
}