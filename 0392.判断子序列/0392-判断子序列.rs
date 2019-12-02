impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        let s_chars: Vec<char> = s.chars().collect();
        let t_chars: Vec<char> = t.chars().collect();
        let mut i  = 0;
        let mut j = 0;
        while i < s_chars.len() && j < t_chars.len() {
            while j < t_chars.len() && t_chars[j] != s_chars[i] {
                j += 1;
            }
            while i < s_chars.len() && j < t_chars.len() && s_chars[i] == t_chars[j] {
                i += 1;
                j += 1;
            }
        }
        
        i == s_chars.len()
    }
}