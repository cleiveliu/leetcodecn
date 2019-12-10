impl Solution {
    pub fn find_content_children(g: Vec<i32>, s: Vec<i32>) -> i32 {
        let mut g = g;
        let mut s = s;
        g.sort();
        s.sort();
        let mut ret = 0;
        let (mut i, mut j) = (0usize, 0usize);
        while i < g.len() && j < s.len() {
            if g[i] <= s[j] {
                ret += 1;
                i += 1;
                j += 1;
            } else {
                j += 1;
            }
        }
        
        ret
    }
}