impl Solution {
    pub fn validate_stack_sequences(pushed: Vec<i32>, popped: Vec<i32>) -> bool {
        let mut stack = vec![];
        let mut i = 0usize;
        for &p in pushed.iter() {
            if p == popped[i] {
                i += 1;
            } else {
                stack.push(p);
            }
            while stack.len() > 0 && stack[stack.len()-1] == popped[i] {
                stack.pop();
                i += 1;
            }
        }
        
        stack.len() == 0
    }
}