impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        if s.len() == 0 {
            return;
        }
        let mut l = 0usize;
        let mut r = s.len()-1;
        while (l < r) {
            let temp = s[l];
            s[l] = s[r];
            s[r] = temp;
            l += 1;
            r -= 1;
        }
    }
}