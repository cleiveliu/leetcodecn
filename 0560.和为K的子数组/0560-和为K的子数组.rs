impl Solution {
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
        let len = nums.len() + 1;
        let mut sums: Vec<i32> = Vec::with_capacity(len);
        sums.push(0);
        for i in 1..len {
            sums.push(sums[i-1] + nums[i-1]);
        }
        println!("{:?}",sums);
        let mut ret = 0;
        for i in 0..sums.len() {
            for j in (i+1)..sums.len() {
                if sums[j] - sums[i] == k {
                    ret += 1;
                }
            }
        }
        
        ret
    }
}