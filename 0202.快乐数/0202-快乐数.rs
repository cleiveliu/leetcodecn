use std::collections::HashSet;
impl Solution {
    pub fn is_happy(n: i32) -> bool {
        let mut seen = HashSet::new();
        let mut n = n;
        while !seen.contains(&n) {
            if n == 1 {
                return true;
            }
            seen.insert(n);
            let mut tmp = 0;
            while n > 0 {
                tmp += (n%10)*(n%10);
                n /= 10;
            }
            n = tmp;
        }
        return false;
    }
}