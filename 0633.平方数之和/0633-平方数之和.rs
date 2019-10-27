impl Solution {
    pub fn judge_square_sum(c: i32) -> bool {
        if c < 0 {
            return false;
        }
        
        let mut left = 0usize;
        let mut right = ((c as f32).sqrt() + 1.0) as usize;
        let c = c as usize;
        while left <= right {
            let val = left*left + right*right;
            if val == c {
                return true;
            } else if val < c {
                left += 1;
            } else {
                right -= 1;
            }
        }
        return false;
    }
}