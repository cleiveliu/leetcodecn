use std::collections::HashSet;
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut ret = 0;
        let mut l = 0;
        let mut set = HashSet::new();
        let chars: Vec<_>  = s.chars().collect();
        for c in chars.iter() {
            while set.contains(c) {
                set.remove(&chars[l]);
                l += 1;
            }
            set.insert(c);
            ret = ret.max(set.len());
        }
        
        ret as i32
    }
}