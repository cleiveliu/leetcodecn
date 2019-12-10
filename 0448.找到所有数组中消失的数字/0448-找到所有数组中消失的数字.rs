impl Solution {
    pub fn find_disappeared_numbers(nums: Vec<i32>) -> Vec<i32> {
        let mut nums = nums;
        for i in 0..nums.len() {
            let index = (nums[i].abs() - 1) as usize;
            nums[index] = -(nums[index].abs());
        }
        let mut ret = vec![];
        for (i, &num) in nums.iter().enumerate() {
            if num > 0 {
                ret.push((i+1) as i32);
            }
        }
        
        ret
    }
}