impl Solution {
    pub fn remove_outer_parentheses(s: String) -> String {
        let mut stack = Vec::new();
        let (mut l, mut r) = (0, 0);
        for c in s.chars() {
            if l == 0 {
                l += 1;
            } else if c == '(' {
                l += 1;
                stack.push(c);
            } else if c == ')' {
                r += 1;
                if l == r {
                    l = 0;
                    r = 0;
                } else {
                    stack.push(c);
                }
            }
        }
        
        stack.iter().collect::<String>()
    }
}