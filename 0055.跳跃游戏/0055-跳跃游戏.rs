impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        if nums.iter().all(|&x| x> 0) {
            return true;
        }
        let mut index = nums.len()-1;
        let mut step = 0;
        while index > 0 {
            index -= 1;
            step += 1;
            if nums[index] >= step {
                step = 0;
            }
        }
        return nums[index] >= step;
    }
}