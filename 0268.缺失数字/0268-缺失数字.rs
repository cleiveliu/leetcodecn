impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let mut ret = nums.len() as i32;
        for i in 0..nums.len() {
            ret ^= (i as i32);
            ret ^= nums[i];
        }
        
        ret
    }
}