impl Solution {
    pub fn find_error_nums(nums: Vec<i32>) -> Vec<i32> {
        let mut ret = vec![0,0];
        let mut cnt = 0;
        let mut nums = nums;
        nums.sort();
        for i in 0..nums.len()-1 {
            if nums[i]+1 != nums[i+1] {
                if nums[i] == nums[i+1] {
                    ret[0] = nums[i];
                    cnt += 1;
                    if cnt >= 2 {
                        break;
                    }
                }
                if nums[i]+2 == nums[i+1] {
                    ret[1] = nums[i] + 1;
                    cnt += 1;
                    if cnt >= 2 {
                        break;
                    }
                }
            }
        }
        if ret[1] == 0 {
            if nums[0] != 1{
                ret[1] = 1;
            } else {
                ret[1] = nums.len() as i32;
            }
        }
        return ret;
    }
}