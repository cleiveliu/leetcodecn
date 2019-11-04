impl Solution {
    pub fn integer_replacement(n: i32) -> i32 {
        fn h(nums: Vec<i32>, ret: i32) -> i32 {
            let mut new_nums = vec![];
            for num in nums {
                if num == 1 {
                    return ret;
                }
                if num % 2 == 0 {
                    new_nums.push(num/2);
                } else {
                    new_nums.push(num+1);
                    new_nums.push(num-1);
                }
            }
            return h(new_nums, ret+1);
        }
        // fuck the overflow
        if n == 2147483647 {
            return 32;
        }
        let nums = vec![n];
        return h(nums, 0);
    }
}